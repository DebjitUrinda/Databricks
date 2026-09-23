# Sort the values in ascending order. Walk through that sorted list and compare every value with the one immediately before it. Return the largest of those differences.

# Produce a single row with one column named max_diff.

# Sort by value, not by id
# "Consecutive" means consecutive in value order. The rows are not stored sorted, so ordering by id gives a different — and wrong — answer.
# Step 1: get each value together with the previous value, in VALUE order.
# Step 2: subtract, and take the largest difference.
# The DataFrame is created for you - do not recreate it.

import pyspark.sql.functions as F
from pyspark.sql import Window

# 1. Define window ordered by value
w = Window.orderBy("value")

# 2. Calculate consecutive difference using lag()
df_diff = numbers.withColumn("previous_value", F.lag("value").over(w)) \
           .withColumn("difference", F.col("value") - F.col("previous_value"))

# 3. Aggregate to find maximum difference and display
df_result = df_diff.select(F.max("difference").alias("max_diff"))
df_result.show()
