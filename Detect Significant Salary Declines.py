# Question (https://pyspark.in/challenges/detect-significant-salary-declines):
# A bank monitors payroll credits to spot customers whose income has fallen sharply, because a sudden drop is an early signal of repayment risk.

# account_transactions holds every transaction on an account. A salary credit is any row where txn_type = 'CREDIT'.

# For each account, compare the latest salary credit against the average of the three salary credits immediately before it. Report the account when that fall is more than 40%.


from pyspark.sql import Window
from pyspark.sql import functions as F
from pyspark.sql.types import DecimalType

filterDf = account_transactions.filter(
      F.col("txn_type") == "CREDIT"
)

w = Window.partitionBy("account_id").orderBy(
      F.col("txn_date").asc()
)

avgprev3salaryDf = filterDf.withColumn("avg_previous_3_salary",
            F.avg("amount").over(w.rowsBetween(-3, -1))
)

salarydropDf = avgprev3salaryDf.withColumn("salary_drop_percentage",
                  (F.col("avg_previous_3_salary")-F.col("amount"))/F.col("avg_previous_3_salary")*100
)

result = salarydropDf.filter(
      F.col("salary_drop_percentage") > 40
)

result = result.withColumn("risk_flag", F.lit("FLAGGED"))

result.select(
    "account_id",
    F.col("avg_previous_3_salary").cast(DecimalType(10, 2)).alias("avg_previous_3_salary"),
    F.col("amount").cast(DecimalType(10, 2)).alias("current_salary"),
    F.col("salary_drop_percentage").cast(DecimalType(10, 2)).alias("salary_drop_percentage"),
    F.lit("FLAGGED").alias("risk_flag")
).show()
