# ==================================================
#               NCFE Data Level 3
#     Unit 3: Assessment 2 - Clustering analysis
# ==================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from adjustText import adjust_text

pd.options.mode.chained_assignment = None

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# Data for the 2025-26 NBA season pulled from basketball reference https://www.basketball-reference.com/leagues/NBA_2026_per_game.html

df = pd.read_csv("bbref_data.csv")

print(df.dtypes)

df.drop(["Age", "G", "GS", "FG", "FGA", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "PF", "Awards", "Player-additional"], axis = 1, inplace = True) # Drop all columns I have no interest in
# The columns that have been retained: Rk (rank), Player, Team, Pos (position), MP (minutes played), FG% (field goal percentage), 3P (3-pointers made), 3PA (3-pointers attempted), 3P% (3-point percentage), TRB (total rebounds), AST (assists), STL (steals), BLK (blocks), TOV (turnovers), PTS (points)
# ==================================================
# I retained a lot of the categories from the original dataset because there are many potentially interesting correlations that can be garnered from the data

pts = df["PTS"]
rank = df["Rk"]
players = df["Player"]
position = df["Pos"]
minutesPlayed = df["MP"]
fgPercentage = df["FG%"]
threesMade = df["3P"]
threesAttempted = df["3PA"]
threePercentage = df["3P%"]
totalRebounds = df["TRB"]
assists = df["AST"]
steals = df["STL"]
blocks = df["BLK"]
turnovers = df["TOV"]

#dfArray = [ptsColumn, threePercentage, threesAttempted, totalRebounds]

'''for x in dfArray :

    df1 = df[df.isna().any(axis = 1)]

    if df1 == True :

        print("test")'''

df1 = df[df.isna().any(axis = 1)]
print(df1)

# By checking for all rows that contain NaN values, we can determine what is the necessary course of action to take for each one.
# We can see that the bottom row is used to contain league averages. For Rk, I will change the value to the median. For the string values (Team, Pos), I will assign them the name League Average.
# For all the other numeric values in that row i.e. the rest of the values, I will calculate the mean value in each column and assign it as league average
# We can see that every other row with a NaN value is in the 3P% column, where the 3PA per game is 0; based on this info, and what we can infer from both the positions of all the players being Centre and what we know about those players and their playstyles is that these players haven't attempted any 3-pointers this season. Using this knowledge, I will change those NaN values to 0, as that is the most suitable adaptation for our purposes.

#print(df)

print(pts.count(), threesAttempted.count())
print(df.dtypes)

# ==================================================
# Calculating and inserting median rank for Rk column
# Replacing string values with "League Average"
# ==================================================

df["Rk"][242] = float("{:.1f}".format((df["Rk"].median())))
df["Team"][242] = "League Average"
df["Pos"][242] = "League Average"

# ==================================================
# Calculating means for each column
# ==================================================

ptsMean = float("{:.1f}".format((pts.mean())))
minutesPlayedMean = float("{:.1f}".format((minutesPlayed.mean())))
threesMadeMean = float("{:.1f}".format((threesMade.mean())))
threesAttemptedMean = float("{:.1f}".format((threesAttempted.mean())))
threePercentageMean = float("{:.1f}".format((threePercentage.mean())))
totalReboundsMean = float("{:.1f}".format((totalRebounds.mean())))
assistsMean = float("{:.1f}".format((assists.mean())))
stealsMean = float("{:.1f}".format((steals.mean())))
blocksMean = float("{:.1f}".format((blocks.mean())))
turnoversMean = float("{:.1f}".format((turnovers.mean())))

# ==================================================
# Inserting means into the league average row
# ==================================================

leagueAvgRow = ["PTS", "MP", "3P", "3PA", "TRB", "AST", "STL", "BLK", "TOV"]
leagueAvgMeans = [ptsMean, minutesPlayedMean, threesMadeMean, threesAttemptedMean, totalReboundsMean, assistsMean, stealsMean, blocksMean, turnoversMean]

i = 0

for x in leagueAvgRow :

    df[x][242] = leagueAvgMeans[i]
    i += 1

i = 0

print(df.loc[[242]])

# ==================================================
# Replacing the NaN values in the 3P% column with 0
# Checking if there are any null values remaining
# ==================================================

df = df.fillna(float("{:.1f}".format(0)))
df1 = df[df.isna().any(axis = 1)]
print(df1)

#exit()

# ==================================================
# Sampling specific data points to illustrate clusters
# ==================================================

dfGuards = df.loc[(df["Pos"] == "PG") | (df["Pos"] == "SG")]
gn = [0,8,48,101,168,192,222]
dfG5 = dfGuards.loc[gn]
print(dfG5)

dfFor = df.loc[(df["Pos"] == "SF") | (df["Pos"] == "PF")]
fn = [4, 23, 56, 113, 137, 205, 225]
dfF5 = dfFor.loc[fn]
print(dfFor)

dfC = df.loc[(df["Pos"] == "C")]
cn = [7, 33, 100, 140, 194, 239]
dfC5 = dfC.loc[cn]
print(dfC)
#exit()

# ==================================================
# Other statistical analysis
# ==================================================

# Variance

ptsVar = pts.var()
threePercentageVar = threePercentage.var()

# Standard Deviation

ptsStd = pts.std()
threePercentageStd = threePercentage.std()

# Correlations

pts_threeAtt = pts.corr(threesAttempted)
pts_totRebounds = pts.corr(totalRebounds)
threeAtt_threePct = threesAttempted.corr(threePercentage)
threeMade_threePct = threesMade.corr(threePercentage)
threeMade_threeAtt = threesMade.corr(threesAttempted)
threeAtt_totRebounds = threesAttempted.corr(totalRebounds)
blocks_totRebounds = blocks.corr(totalRebounds)
steals_ast = steals.corr(assists)
tov_ast = turnovers.corr(assists)
mp_pts = minutesPlayed.corr(pts)
fgp_totRebounds = fgPercentage.corr(totalRebounds)

print(f"Average points per game: {ptsMean}\nPoints per game variance: {ptsVar}\nPPG standard deviation: {ptsStd}\nAverage 3 point percentage: {threePercentageMean}\n3P% variance: {threePercentageVar}\n3P% standard deviation: {threePercentageStd}")

print(f"Correlation between points scored and threes attempted: {pts_threeAtt}\nCorrelation between points and total rebounds: {pts_totRebounds}\nCorrelation between threes attempted and three point percentage: {threeAtt_threePct}\nCorrelation between threes made and three point percentage: {threeMade_threePct}\nCorrelation between threes made and threes attempted: {threeMade_threeAtt}\nCorrelation between threes attempted and total rebounds: {threeAtt_totRebounds}\nCorrelation between blocks and total rebounds: {blocks_totRebounds}\nCorrelation between steals and assists: {steals_ast}\nCorrelation between turnovers and assists: {tov_ast}\nCorrelation between minutes played and points: {mp_pts}\nCorrelation between field-goal percentage and total rebounds: {steals_ast}")

#print(df)

plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
sns.histplot(data = df, x="FG%", y="3PA", kde=True, color="blue")
plt.title("FG% compared to 3P taken")

plt.subplot(1, 2, 2)
sns.histplot(data = df, x="FG%", y="TRB", kde=True, color="pink")
plt.title("FG% compared to Tot. Rebounds")

plt.tight_layout()
plt.show()
# exit()

X = df[["PTS", "FG%"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X)
print(X_scaled)

kmeans = KMeans(n_clusters=5, init = "k-means++", random_state=42)

clusters = kmeans.fit_predict(X_scaled)
df["Cluster"] = clusters

colours = ["#333366", "#d6cadd", "#789bd1", "#c1d7ee", "#a743ba"]

plt.subplot(2, 2, 1)

plt.title("Points scored against shooting percentage")
sns.scatterplot(data = df, x = "PTS", y="FG%", hue = "Cluster", palette=sns.color_palette(colours, len(colours)))

plt.subplot(2, 2, 2)

plt.title("Guard labels")
for idx, row in dfG5.iterrows(): # USE WHEN I WANT TO SHOW PLAYER NAMES TO ILLUSTRATE VALIDITY OF DATA

    plt.annotate(row['Player'], (row['PTS'], row['FG%']), xytext=(15,180), textcoords="offset pixels", arrowprops=dict(width = 0.2, headwidth = 3, headlength = 5, facecolor='black', shrink=0.05), fontsize = 7)

sns.scatterplot(data = df, x = "PTS", y="FG%", hue = "Cluster", palette=sns.color_palette(colours, len(colours)))

plt.subplot(2, 2, 3)

plt.title("Forwards labels")
for idx, row in dfF5.iterrows(): # USE WHEN I WANT TO SHOW PLAYER NAMES TO ILLUSTRATE VALIDITY OF DATA

    plt.annotate(row['Player'], (row['PTS'], row['FG%']), xytext=(15,180), textcoords="offset pixels", arrowprops=dict(width = 0.2, headwidth = 3, headlength = 5, facecolor='black', shrink=0.05), fontsize = 7)

sns.scatterplot(data = df, x = "PTS", y="FG%", hue = "Cluster", palette=sns.color_palette(colours, len(colours)))

plt.subplot(2, 2, 4)

plt.title("Centers labels")
for idx, row in dfC5.iterrows(): # USE WHEN I WANT TO SHOW PLAYER NAMES TO ILLUSTRATE VALIDITY OF DATA

    plt.annotate(row['Player'], (row['PTS'], row['FG%']), xytext=(15,90), textcoords="offset pixels", arrowprops=dict(width = 0.2, headwidth = 3, headlength = 5, facecolor='black', shrink=0.05), fontsize = 7)

sns.scatterplot(data = df, x = "PTS", y="FG%", hue = "Cluster", palette=sns.color_palette(colours, len(colours)))

# wcss = []

# for i in range(1, 11) :

#     kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
#     kmeans.fit(X_scaled)
#     wcss.append(kmeans.inertia_)

# plt.figure(figsize=(10, 6))
# plt.plot(range(1, 11), wcss, marker = 'x', linestyle = "--")
# plt.show()

plt.figure(figsize=(10, 7))
sns.scatterplot(data = df, x="PTS", y="FG%", hue="Cluster", s=100, alpha=0.8, palette=sns.color_palette(colours, len(colours)))

centres = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centres[:, 0], centres[:, 1], s=300, c="red", marker="o", label = "Centroids")
plt.legend()

plt.show()

target_group = df[df["Cluster"] == 1]
print(f"Number of target group: {len(target_group)}")