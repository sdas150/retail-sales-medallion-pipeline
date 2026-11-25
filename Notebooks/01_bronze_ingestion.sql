-- Upload data/sales.csv and create workspace.bronze_retail.sales_csv first.
SELECT COUNT(*) AS bronze_record_count FROM workspace.bronze_retail.sales_csv;
SELECT * FROM workspace.bronze_retail.sales_csv ORDER BY order_id;
