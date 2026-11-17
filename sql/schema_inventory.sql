-- Read-only schema inventory; run in an explicitly authorized schema via SQLcl.
-- No database object is created or changed. No table contents are selected.
-- For complete metadata, grants must allow visibility of the target objects.
SET PAGESIZE 500 LINESIZE 200
PROMPT === TABLES/COLUMNS visible to current user ===
SELECT table_name, column_id, column_name, data_type, nullable
  FROM user_tab_columns
 ORDER BY table_name, column_id;
PROMPT === CONSTRAINTS ===
SELECT table_name, constraint_name, constraint_type, status, r_constraint_name
  FROM user_constraints ORDER BY table_name, constraint_name;
PROMPT === INDEXES ===
SELECT table_name, index_name, uniqueness, status
  FROM user_indexes ORDER BY table_name, index_name;
