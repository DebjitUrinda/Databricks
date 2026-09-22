# You are given matches, one row per completed match between two teams.

# For every team that played at least one match, report its record:

# Column	Meaning
# team	the team name
# total_match	matches played, whether it appeared as team1 or team2
# win_count	matches where team = winner
# lose_count	matches it played but did not win

# Tables & Schema:

# ⬡ Table: `matches`
# Column	Type	Description
# team1	VARCHAR	first participating team
# team2	VARCHAR	second participating team
# winner	VARCHAR	the winning team

# Constraints:
# A team can appear in either team1 or team2.
# Every match counts once toward the total of both participants.
# A team wins when team = winner; the other participant takes the loss.
# Include every team that played at least one match.
# Do not hardcode team names. The query must work for any set of teams.
# Return rows sorted by team ascending.

from pyspark.sql import functions as F

teams = matches.select(F.col("team1").alias("team")).union\
(matches.select(F.col("team2").alias("team")))

total_matches = teams.groupBy("team").agg(
     F.count("*").alias("total_match")
)

wins = matches.select(F.col("winner").alias("team")).groupBy("team").agg(
     F.count("*").alias("win_count")
)

result = total_matches.join(
     wins,
     on="team",
     how="left"
)

result = result.withColumn("lose_count", F.col("total_match")-F.col("win_count"))

result.show()
