# Flag each user as retained (1) or not (0) on day 1, 7 and 30 after
# their OWN signup date. Users who never returned still appear, as zeros.
# Also add retention_pattern: the three flags joined by '-', e.g. '1-0-0'.

joined = signups.join(user_events, "user_id", "left").\
orderBy(F.col("user_id").asc(), F.col("event_date").asc())

df_offset = joined.withColumn("offset", F.datediff("event_date", "signup_date"))

df_D = df_offset.groupBy("user_id")\
    .pivot("offset", [1,7,30])\
    .agg(F.max(F.lit(1)))\
    .fillna(0)

df_result = df_D.select("user_id", F.col("1").alias("retained_d1"),\
            F.col("7").alias("retained_d7"),\
            F.col("30").alias("retained_d30")).\
            withColumn("retention_pattern", \
            F.concat(F.col("retained_d1"),F.lit("-"),\
            F.col("retained_d7"),F.lit("-"),F.col("retained_d30")))

df_result.show()
