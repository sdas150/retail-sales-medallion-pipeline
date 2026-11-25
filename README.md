# Retail Sales Medallion Pipeline

Beginner Databricks Data Engineering project using Python/PySpark, SQL, Delta tables, Bronze/Silver/Gold architecture, data-quality checks, quarantine handling, Gold aggregations, and an educational partitioning exercise.

## Run order
1. sql/01_create_schemas.sql
2. Upload data/sales.csv and create workspace.bronze_retail.sales_csv
3. notebooks/01_bronze_ingestion.sql
4. notebooks/02_bronze_to_silver.py
5. sql/02_silver_validation.sql
6. notebooks/03_silver_to_gold.sql
7. sql/03_gold_validation.sql
8. notebooks/04_partitioning_exercise.py
9. notebooks/05_data_quality_tests.py
10. Create a Databricks Job/Workflow using the same dependency order.

## Expected reconciliation
30 raw = 1 exact duplicate + 7 quarantine + 22 Silver clean.

## Status
Core Bronze, Silver and Gold work is complete. Partitioning, automated test execution, and the Databricks workflow are supplied as next-step material and still need to be run/configured in your workspace.

See docs/revision_notes.md and docs/test_cases.md for revision and analysis.
