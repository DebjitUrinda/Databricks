# Count customers who were active in a month but absent the next one.
# The first month has nothing before it and the last month has nothing
# after it — neither should produce a row.

from pyspark.sql import functions as F
from pyspark.sql import Window

w_month = Window.orderBy("month_num")

monthly_count = monthly_active.groupBy("month_num").agg(
    F.collect_list("customer_id").alias("customer_list")
)

df_lagged = monthly_count.withColumn(
    "prev_list", F.lag("customer_list", 1).over(w_month)
).filter(F.col("prev_list").isNotNull())

df_churn = df_lagged.withColumn(
    "Churn_count", F.array_except(F.col("prev_list"), F.col("customer_list"))
)

df_result = df_churn.select("month_num", F.array_size("churn_count").alias("churned_customers"))

df_result.show()
