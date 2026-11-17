"""Redistributable synthetic export examples. No customer or Oracle-owned export."""
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from apex_devkit.cli import main
from apex_devkit.exports import inspect_export, inspect_text


SYNTHETIC_EXPORT = """-- Synthetic APEX export declaration fixture.
wwv_flow_imp_page.create_page(p_id=>1);
wwv_flow_imp_page.create_page_plug(p_id=>2);
wwv_flow_imp_page.create_report_region(p_id=>3);
wwv_flow_imp_page.create_page_item(p_id=>4);
wwv_flow_imp_page.create_page_button(p_id=>5);
wwv_flow_imp_page.create_page_da_event(p_id=>6);
wwv_flow_imp_page.create_page_process(p_id=>7);
wwv_flow_imp_shared.create_list_of_values(p_id=>8);
-- wwv_flow_imp_page.create_page(p_id=>999);
select q'[wwv_flow_imp_page.create_report_region(p_id=>1000);]' from dual;
"""

EXPECTED = {
    "pages": 1,
    "regions": 1,
    "report_regions": 1,
    "page_items": 1,
    "buttons": 1,
    "dynamic_actions": 1,
    "page_processes": 1,
    "shared_lovs": 1,
}


class SyntheticExportRegressionTests(unittest.TestCase):
    def test_signature_counts_ignore_comments_and_quoted_sql(self):
        counts, findings = inspect_text(SYNTHETIC_EXPORT, "synthetic.sql")
        self.assertEqual(dict(counts), EXPECTED)
        self.assertEqual(findings, [])

    def test_single_sql_and_zip_produce_same_counts(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            sql = root / "synthetic.sql"
            sql.write_text(SYNTHETIC_EXPORT, encoding="utf-8")
            archive = root / "synthetic.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                zf.writestr("app/page_00001.sql", SYNTHETIC_EXPORT)
            self.assertEqual(inspect_export(sql)["components"], EXPECTED)
            self.assertEqual(inspect_export(archive)["components"], EXPECTED)
            self.assertEqual(inspect_export(archive)["files_inspected"], 1)

    def test_lint_line_numbers_across_large_multiline_input(self):
        from apex_devkit.analysis import analyze_sql
        source = ("-- ignored\n" * 1000) + "SELECT * FROM records;\n" + ("\n" * 1000) + "COMMIT;"
        findings = analyze_sql(source)
        self.assertEqual([(item.rule, item.line) for item in findings],
                         [("SQL001", 1001), ("SQL003", 2002)])

    def test_zip_byte_budget_counts_exact_source_bytes(self):
        from apex_devkit.exports import _read_bounded
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / "bytes.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("plain.sql", b"abc")
                zf.writestr("bom.sql", b"\xef\xbb\xbfabc")
            with zipfile.ZipFile(archive) as zf:
                plain, plain_bytes = _read_bounded(zf, zf.getinfo("plain.sql"), 3)
                bom, bom_bytes = _read_bounded(zf, zf.getinfo("bom.sql"), 6)
                self.assertEqual((plain, plain_bytes), ("abc", 3))
                self.assertEqual((bom, bom_bytes), ("abc", 6))
                with self.assertRaises(ValueError):
                    _read_bounded(zf, zf.getinfo("bom.sql"), 5)

    def test_split_directory_and_cli_json(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            export_dir = root / "split"
            export_dir.mkdir()
            (export_dir / "page.sql").write_text(SYNTHETIC_EXPORT, encoding="utf-8")
            (export_dir / "notes.txt").write_text("not SQL", encoding="utf-8")
            report = root / "report.json"
            self.assertEqual(main(["inspect-export", str(export_dir), "--format", "json",
                                   "--output", str(report)]), 0)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(data["components"], EXPECTED)
            self.assertEqual(data["files_inspected"], 1)


if __name__ == "__main__":
    unittest.main()
