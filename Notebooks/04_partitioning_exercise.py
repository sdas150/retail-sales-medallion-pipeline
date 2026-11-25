from pyspark.sql import functions as F
# Learning exercise only: this tiny dataset does not need partitioning for performance.
partitioned_df = (spark.table("workspace.silver_retail.sales_clean")
    .withColumn("order_year", F.year("order_date"))
    .withColumn("order_month", F.month("order_date")))
(partitioned_df.write.format("delta").mode("overwrite")
    .partitionBy("order_year", "order_month")
    .saveAsTable("workspace.silver_retail.sales_partitioned"))
