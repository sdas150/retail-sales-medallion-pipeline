SELECT COUNT(*) total_records, COUNT(DISTINCT order_id) unique_orders,
SUM(CASE WHEN customer_id IS NULL OR TRIM(customer_id)='' THEN 1 ELSE 0 END) missing_customers,
SUM(CASE WHEN product IS NULL OR TRIM(product)='' THEN 1 ELSE 0 END) missing_products,
SUM(CASE WHEN quantity<=0 THEN 1 ELSE 0 END) invalid_quantity,
SUM(CASE WHEN unit_price<=0 THEN 1 ELSE 0 END) invalid_price,
SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END) invalid_dates
FROM workspace.silver_retail.sales_clean;
SELECT order_id,customer_id,product,quantity,unit_price,order_date,rejection_reason
FROM workspace.silver_retail.sales_quarantine ORDER BY order_id;
