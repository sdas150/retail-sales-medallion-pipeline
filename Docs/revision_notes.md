# Revision Notes

## What is completed
- Created workspace.bronze_retail, workspace.silver_retail, workspace.gold_retail.
- Loaded sales.csv into workspace.bronze_retail.sales_csv: 30 rows.
- Removed one exact duplicate: 29 rows remain.
- Standardized text with trim/initcap and accepted yyyy-MM-dd plus yyyy/MM/dd dates.
- Applied data-quality rules for customer, product, quantity, price, and date.
- Wrote 22 valid rows to sales_clean and 7 invalid rows to sales_quarantine with reasons.
- Added total_amount = quantity * unit_price.
- Created daily_sales, product_sales, customer_sales Gold tables.
- Manual Silver checks showed 22 total, 22 unique, zero missing customers/products, zero invalid quantities/prices.
- Observed Gold examples: Laptop revenue 453000; Mouse units sold 11; customer C018 total_spent 128000.

## Still to do in Databricks
1. Run 04_partitioning_exercise.py and verify sales_partitioned.
2. Run 05_data_quality_tests.py and make sure all tests PASS.
3. Build a Databricks Job/Workflow in this order: Bronze verification/ingestion -> Bronze-to-Silver -> Gold -> tests.
4. Export/commit the project to GitHub if desired.

## Key explanation for revision/interview
Bronze preserves raw source data. Silver uses PySpark for cleaning, standardization, validation, calculations, and quarantine. Gold uses SQL aggregations for reporting. Reconciliation/testing proves rows are accounted for rather than silently lost.
