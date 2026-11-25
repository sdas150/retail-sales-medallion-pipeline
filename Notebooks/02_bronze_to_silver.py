from pyspark.sql import functions as F
bronze_df = spark.table("workspace.bronze_retail.sales_csv")
silver_df = bronze_df.dropDuplicates()
silver_df = (silver_df
    .withColumn("customer_id", F.trim(F.col("customer_id")))
    .withColumn("product", F.initcap(F.trim(F.col("product"))))
    .withColumn("category", F.initcap(F.trim(F.col("category"))))
    .withColumn("city", F.initcap(F.trim(F.col("city")))))
silver_df = silver_df.withColumn("clean_order_date", F.coalesce(
    F.try_to_date(F.col("order_date"), F.lit("yyyy-MM-dd")),
    F.try_to_date(F.col("order_date"), F.lit("yyyy/MM/dd"))))
valid_condition = (
    F.col("customer_id").isNotNull() & (F.trim(F.col("customer_id")) != "") &
    F.col("product").isNotNull() & (F.trim(F.col("product")) != "") &
    F.col("quantity").isNotNull() & (F.col("quantity") > 0) &
    F.col("unit_price").isNotNull() & (F.col("unit_price") > 0) &
    F.col("clean_order_date").isNotNull())
valid_df = silver_df.filter(valid_condition)
invalid_df = silver_df.filter(~valid_condition)
invalid_df = invalid_df.withColumn("rejection_reason", F.concat_ws("; ",
    F.when(F.col("customer_id").isNull() | (F.trim(F.col("customer_id")) == ""), F.lit("Missing customer_id")),
    F.when(F.col("product").isNull() | (F.trim(F.col("product")) == ""), F.lit("Missing product")),
    F.when(F.col("quantity").isNull() | (F.col("quantity") <= 0), F.lit("Invalid quantity")),
    F.when(F.col("unit_price").isNull() | (F.col("unit_price") <= 0), F.lit("Invalid unit_price")),
    F.when(F.col("clean_order_date").isNull(), F.lit("Invalid order_date"))))
valid_df = (valid_df.drop("order_date")
    .withColumnRenamed("clean_order_date", "order_date")
    .withColumn("total_amount", F.col("quantity") * F.col("unit_price")))
valid_df.write.format("delta").mode("overwrite").saveAsTable("workspace.silver_retail.sales_clean")
invalid_df.write.format("delta").mode("overwrite").saveAsTable("workspace.silver_retail.sales_quarantine")
