import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from apex_devkit.analysis import analyze_sql, mask_sql
from apex_devkit.exports import inspect_export
from apex_devkit.cli import main, to_markdown

class ToolkitTests(unittest.TestCase):
    def test_mask_ignores_comments_and_literals(self):
        text = "-- SELECT * FROM t\nSELECT '*' as x FROM t; /* EXECUTE IMMEDIATE */"
        self.assertEqual(analyze_sql(text), [])
        self.assertEqual(mask_sql(text).count('\n'), text.count('\n'))
    def test_rules(self):
        f = analyze_sql('SELECT * FROM employees;\nEXECUTE IMMEDIATE statement;\nWHEN OTHERS THEN NULL;')
        self.assertEqual([x.rule for x in f], ['SQL001', 'SEC001', 'SEC002'])
    def test_suppression_and_disable(self):
        self.assertFalse(analyze_sql('SELECT * FROM t; -- devkit: ignore SQL001'))
        self.assertFalse(analyze_sql('SELECT * FROM t;', disabled={'SQL001'}))
    def test_export_single(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/'f1.sql'
            p.write_text('wwv_flow_imp_page.create_page(p_id=>1);\n-- wwv_flow_imp_page.create_page(p_id=>2);\nwwv_flow_imp_page.create_page_item(p_id=>3);')
            r = inspect_export(p)
            self.assertEqual(r['components'], {'page_items': 1, 'pages': 1})
    def test_zip_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/'bad.zip'
            with zipfile.ZipFile(p, 'w') as z:
                z.writestr('../evil.sql', 'wwv_flow_imp_page.create_page(')
            with self.assertRaises(ValueError):
                inspect_export(p)
    def test_zip_split(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/'okay.zip'
            with zipfile.ZipFile(p,'w') as z:
                z.writestr('f1/application/pages/page_00001.sql', 'wwv_flow_imp_page.create_page(p_id=>1);')
            self.assertEqual(inspect_export(p)['components']['pages'], 1)
    def test_cli_json(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/'sample.sql'; out = Path(td)/'report.json'
            p.write_text('SELECT * FROM dual;')
            self.assertEqual(main(['lint', str(p), '--format', 'json', '--output', str(out)]), 0)
            self.assertEqual(json.loads(out.read_text())['findings'][0]['rule'], 'SQL001')
    def test_cli_rejects_wrong_file(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'a.txt'; p.write_text('bad')
            self.assertEqual(main(['lint', str(p)]), 2)
    def test_markdown_report(self):
        self.assertIn('No matching advisory', to_markdown({'kind':'sql-static','findings':[],'limitations':'Limited'}))

if __name__ == '__main__': unittest.main()

class AdditionalSafetyTests(unittest.TestCase):
    def test_bad_zip_backslash(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/'bad.zip'
            with zipfile.ZipFile(p, 'w') as z:
                z.writestr('..\\evil.sql', 'x')
            with self.assertRaises(ValueError):
                inspect_export(p)
    def test_zip_total_size_limit(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'oversized.zip'
            with zipfile.ZipFile(p, 'w', compression=zipfile.ZIP_DEFLATED) as z:
                z.writestr('large.sql', 'x' * (20 * 1024 * 1024 + 1))
            with self.assertRaises(ValueError):
                inspect_export(p)
    def test_unknown_export_does_not_fabricate(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'none.sql'; p.write_text('begin null; end;')
            self.assertEqual(inspect_export(p)['components'], {})

class HardeningTests(unittest.TestCase):
    def test_oracle_alternative_quotes_are_masked(self):
        for literal in ["q'[SELECT * FROM users]'", "Q'{EXECUTE IMMEDIATE x}'",
                        "q'(WHEN OTHERS THEN)'", "q'<COMMIT;>'", "q'!SELECT * FROM t!'"]:
            with self.subTest(literal=literal):
                self.assertEqual(analyze_sql('select ' + literal + ' from dual;'), [])
                self.assertEqual(len(mask_sql(literal)), len(literal))

    def test_qquote_preserves_line_offsets(self):
        sql = "select q'[hello\nSELECT * FROM secret]' from dual;\nSELECT * FROM real_table;"
        findings = analyze_sql(sql)
        self.assertEqual([(f.rule, f.line) for f in findings], [('SQL001', 3)])

    def test_zip_symlink_rejected(self):
        import stat
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / 'symlink.zip'
            with zipfile.ZipFile(p, 'w') as z:
                info = zipfile.ZipInfo('link.sql')
                info.create_system = 3
                info.external_attr = (stat.S_IFLNK | 0o777) << 16
                z.writestr(info, 'target.sql')
            with self.assertRaisesRegex(ValueError, 'symlinks'):
                inspect_export(p)

    def test_directory_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / 'safe.sql').write_text('wwv_flow_imp_page.create_page(p_id=>1);')
            (root / 'alias.sql').symlink_to('safe.sql')
            with self.assertRaisesRegex(ValueError, 'Symlinks'):
                inspect_export(root)

    def test_zip_drive_prefix_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / 'drive.zip'
            with zipfile.ZipFile(p, 'w') as z:
                z.writestr('C:/private.sql', 'x')
            with self.assertRaisesRegex(ValueError, 'Unsafe'):
                inspect_export(p)


class RealExportSignatureTests(unittest.TestCase):
    def test_report_region_distinguished(self):
        from apex_devkit.exports import inspect_text
        fixture = (
            'wwv_flow_imp_page.create_page_plug(p_id=>1);\n'
            'wwv_flow_imp_page.create_report_region(p_id=>2);\n'
            'wwv_flow_imp_page.create_page(p_id=>3);\n'
        )
        counts, findings = inspect_text(fixture, 'synthetic.sql')
        self.assertEqual(counts['regions'], 1)
        self.assertEqual(counts['report_regions'], 1)
        self.assertEqual(counts['pages'], 1)
        self.assertEqual(findings, [])
