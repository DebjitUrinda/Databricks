# For each region, find the three customers who spent the most in total.

# A customer's total is the sum of amount across all of their sales rows.

# If a region has fewer than three customers, return all of them.

# Tables & Schema
# customers

# Column	Type
# customer_id	int
# customer_name	string
# region	string
# sales

# Column	Type
# sale_id	int
# customer_id	int
# amount	int
# Step 1: join sales to customers and total each customer's amount.
# Step 2: rank those totals inside each region and keep the top 3.
# The DataFrames are created for you - do not recreate them.

w_cust = Window.partitionBy("customer_id")
total_amount = sales.select("customer_id", "amount").withColumn(
    "total_amount", F.sum(F.col("amount")).over(w_cust))

total_amount = total_amount.select("customer_id", "total_amount").distinct()

w_region = Window.partitionBy("region").orderBy(F.col("total_amount").desc())
joined_df = customers.join(total_amount, on="customer_id", how="left")

df_result = joined_df.select("region", "customer_name", "total_amount").withColumn(
    "rn", F.row_number().over(w_region)).filter(F.col("rn") <= 3).drop(F.col("rn"))

df_result.show()
