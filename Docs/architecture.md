# Architecture

sales.csv -> workspace.bronze_retail.sales_csv (30 raw)
-> PySpark cleanup/validation
   -> workspace.silver_retail.sales_clean (22 valid)
   -> workspace.silver_retail.sales_quarantine (7 invalid)
-> SQL aggregation
   -> workspace.gold_retail.daily_sales
   -> workspace.gold_retail.product_sales
   -> workspace.gold_retail.customer_sales

One exact duplicate is removed during Bronze-to-Silver processing.
