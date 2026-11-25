CREATE OR REPLACE TABLE workspace.gold_retail.daily_sales AS
SELECT order_date, COUNT(DISTINCT order_id) total_orders, SUM(quantity) total_quantity,
       SUM(total_amount) total_revenue, AVG(total_amount) average_order_value
FROM workspace.silver_retail.sales_clean GROUP BY order_date;

CREATE OR REPLACE TABLE workspace.gold_retail.product_sales AS
SELECT product, COUNT(DISTINCT order_id) total_orders, SUM(quantity) units_sold,
       SUM(total_amount) total_revenue, AVG(unit_price) average_unit_price
FROM workspace.silver_retail.sales_clean GROUP BY product;

CREATE OR REPLACE TABLE workspace.gold_retail.customer_sales AS
SELECT customer_id, COUNT(DISTINCT order_id) total_orders, SUM(quantity) total_items,
       SUM(total_amount) total_spent, AVG(total_amount) average_order_value
FROM workspace.silver_retail.sales_clean GROUP BY customer_id;
