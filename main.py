import pandas as pd
import numpy as np
# Mini NBA Drill – Your Table
# 1. Basic inspection

# Load the CSV into pandas.
df = pd.read_csv("nba.csv")

# Print the first 5 rows, shape, and column names.
print(f"The first five rows of this data frame are \n{df.head()}")
print(f"The shape of this data frame is {df.shape}")
print(f"The columns of this data frame are {df.columns}")
# Check for missing values per column.
num_missing_vals = df.isna().sum()
print(f"The number of missing values per columns are: \n{num_missing_vals}")
# 2. Filtering

# Show all players with a Salary > 10,000,000.
rich_players = df.loc[df["Salary"] > 10000000]
print(f"All players with a salary greater than 10 million are: \n{rich_players}")
# Show all players from "Boston Celtics" who are younger than 25.
young_celtics = df.loc[(df["Team"] == "Boston Celtics") & (df["Age"] < 25)]
print(f"All players on the Celtics younger than 25 are: \n{young_celtics}")
# Using .query(), show players who are PG or SG and Age < 25.
young_guards = df.query("(Position == 'PG' or Position == 'SG') and Age < 25")
print(f"All players who are guards and younger than 25 are {young_guards}")
# 3. Derived columns

# Create Salary_in_Millions = Salary / 1_000_000.
df["Salary_in_Millions"] = df["Salary"] / 1000000
# Create IsYoungStar = True if Age < 25 and Salary_in_Millions > 5.
df["IsYoungStar"] = (df["Age"] < 25) & (df["Salary_in_Millions"] > 5)


# Create BigMan = True if Position is "C" or "PF" and Height > "6-9" (you’ll need to convert height to inches).
def height_to_inches(height):
    inches = 0
    if len(height) == 3:
        inches += int(height[-1])
    elif len(height) == 4:
        inches += int(height[-2:])
    else:
        raise ValueError("Invalid height arguement")
    # an nba player being 10 feet tall is not practical, only check for 3 or 4 characters
    inches += 12 * int(height[0])
    return inches


df["Inches"] = df["Height"].apply(height_to_inches)
df["BigMan"] = ((df["Position"] == "C") | (df["Position"] == "PF")) & (
    df["Inches"] > height_to_inches("6-9")
)

# 4. Aggregation
# Average Salary_in_Millions by Team.
avg_salary_by_team = df.groupby("Team")["Salary"].agg("mean")
print(f"The average salary by team is: \n{avg_salary_by_team}")
# Count of BigMan players by Team.
num_bigman_per_team = df.groupby("Team")["BigMan"].agg("sum")
print(f"The numbers of big men for each team are: \n{num_bigman_per_team}")
# Average Age per Position.
avg_age_by_position = df.groupby("Position")["Age"].agg("mean")
print(f"The average age per each position are: \n{avg_age_by_position}")
# 5. Sorting / ranking

# Top 5 highest paid players.
richest_players = df.sort_values("Salary", ascending=False).head()
print(f"The top 5 highest paid players are: \n{richest_players}")
# Top 5 youngest PGs.
youngest_pgs = df.loc[df["Position"] == "PG"].sort_values("Age").head()
print(f"The top 5 youngest PGs are: \n{youngest_pgs}")
# Team with the highest average Salary_in_Millions.

richest_team = avg_salary_by_team.sort_values(ascending=False).index[0]
print(f"The team with the highest average salary in millions is the: {richest_team}")
# 6. Insight

# Write one sentence about which teams pay the most, or which players stand out financially or age-wise.
# I found a wide variety of insights, including the Caviliers spending the most money on their players,
# the average age for centers being the highest in the league of all posiitons, and Kobe being the 
# highest paid player in the league with a salary of 25 million