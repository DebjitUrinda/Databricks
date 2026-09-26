# For each date, how many DISTINCT customers have been active up to and
# including it. The number never goes down. One row per date.

w = Window.orderBy("activity_date")\
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

dates = user_activity.select("activity_date").distinct()

first_active = user_activity.groupBy("customer_id").agg(
    F.min("activity_date").alias("first_active_date")
)

new_users = first_active.groupBy("first_active_date").agg(
    F.count("customer_id").alias("new_users")
)

daily = dates.join(new_users,
        dates.activity_date == new_users.first_active_date,
        "left"
).select(dates.activity_date, "new_users").fillna(0).orderBy("activity_date")

df_result = daily.withColumn("cumulative_users", F.sum("new_users").over(w)).\
        select("activity_date", "cumulative_users")
        

df_result.show()
