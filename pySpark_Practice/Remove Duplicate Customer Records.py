# A data-ingestion fault inserted some customers more than once.

# Two rows are duplicates only when all three of these are identical: customer_name, email, phone.

# Keep exactly one row per customer: the one with the smallest customer_id.

# Tables & Schema
# Column	Type
# customer_id	int
# customer_name	string
# email	string
# phone	string
# Example
# customer_id	customer_name	email	phone
# 101	Alice	alice@mail.com	555-3311
# 102	Bob	bob@mail.com	555-3322
# 103	Alice	alice@mail.com	555-3311
# 104	Carol	carol@mail.com	555-3333
# 105	Bob	bob@mail.com	555-3322
# 106	Alice	alice@mail.com	555-3311
# 107	Dan	dan@mail.com	555-3344
# 108	Dan	dan@mail.com	555-3399
# Expected Output
# customer_id	customer_name	email	phone
# 101	Alice	alice@mail.com	555-3311
# 102	Bob	bob@mail.com	555-3322
# 104	Carol	carol@mail.com	555-3333
# 107	Dan	dan@mail.com	555-3344
# 108	Dan	dan@mail.com	555-3399
# Explanation
# Alice appears three times — ids 101, 103 and 106 — with the same name, email and phone. Keep id 101, the smallest. Drop 103 and 106.

# Bob appears twice — ids 102 and 105. Keep id 102.

# Carol appears once — keep it.

# Dan is the interesting one. Ids 107 and 108 share a name and an email, but the phones differ: 555-3344 against 555-3399. All three columns must match for a row to be a duplicate, so these are two different records and both are kept.

# 5 rows survive out of 8.

# A note on dropDuplicates
# customers.dropDuplicates(["customer_name", "email", "phone"]) keeps an arbitrary row from each group. On a small local DataFrame it often happens to keep the first one, but that is not guaranteed once the data is partitioned and shuffled, so it is not a safe way to say "keep the smallest id". row_number() ordered by customer_id makes the choice explicit.

# Constraints
# The DataFrame is created for you — do not recreate it
# Build a DataFrame called df_result and finish with df_result.show()
# Output exactly the four original columns, ordered by customer_id ascending
# Drop the helper rank column before showing
# Same problem in SQL: [Remove Duplicate Customer Records](/challenges/remove-duplicate-customer-records)
# Production Constraints
# A row counts as a duplicate only when name, email, AND phone all match another row -- matching on just name and email is not enough.
# Exactly the four original columns are returned, ordered by customer_id ascending, with no helper ranking column left behind.

"""
NOTE: customers.dropDuplicates(["customer_name", "email", "phone"]) keeps an arbitrary row from each group. On a small local DataFrame it often happens to keep the first one, but that is not guaranteed once the data is partitioned and shuffled, so it is not a safe way to say "keep the smallest id". row_number() ordered by customer_id makes the choice explicit.
"""

import pyspark.sql.functions as F
from pyspark.sql import Window

w = Window.partitionBy("customer_name", "email", "phone").orderBy("customer_id")

df_rank = customers.withColumn("rn", F.row_number().over(w)).filter(F.col("rn")==1).drop(F.col("rn"))

df_rank.show()
