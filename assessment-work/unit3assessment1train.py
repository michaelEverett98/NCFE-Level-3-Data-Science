# ==================================================
#               NCFE Data Level 3
#       Unit 3: Assessment 1 - Linear regression
#            and statistical modelling
# ==================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
import statsmodels.api as sm

#pd.set_option("display.max_rows", None)

data = pd.read_csv("song_stats_sheet.csv")
df = pd.DataFrame(data._data)

print(df.dtypes) # Check the column headers and data types

df.drop(["Artist","Year", "Unnamed: 4", "R#", "Rate", "/", "Unnamed: 10", "11s", "≥10", "≥9", "<5", "<3", "0s", "P#", "Unnamed: 18", "11%", "≥10%", "<3%", "0%", "Unnamed: 25", "Bonus", "Date", "ID", "CU", "ArtistList", "Win"], axis = 1, inplace = True) # Drop all columns I have no interest in
df["≥9%"] = df["≥9%"].str.replace("%", "").astype(float)
df["<5%"] = df["<5%"].str.replace("%", "").astype(float)
print(df.dtypes)

# X = df
#y = df.target
# df['target'] = data.target

# print(df)
# exit()

scoreColumn = df["Score"]
controversyColumn = df["Controv."]
highScoresCol = df["≥9%"]
lowScoresCol = df["<5%"]
#print(scoreColumn.type())

print(scoreColumn.count(), highScoresCol.count()) # Checking the dimensions of the data array
averageScore = float("{:.3f}".format((scoreColumn.mean())))
averageControversy = float("{:.2f}".format((controversyColumn.mean())))
scoreVariance = float("{:.3f}".format((scoreColumn.var())))
controversyVariance = float("{:.2f}".format((controversyColumn.var())))
scoreStd = float("{:.3f}".format((scoreColumn.std())))
controversyStd = float("{:.2f}".format((controversyColumn.std())))

print(f"Average score: {averageScore}\nScore variance: {scoreVariance}\nScore standard deviation: {scoreStd}\nAverage controversy: {averageControversy}\nControversy variance: {controversyVariance}\nControversy standard deviation: {controversyStd}")

correlationHighScores = float("{:.2f}".format((scoreColumn.corr(highScoresCol))))
correlationLowScores = float("{:.2f}".format((scoreColumn.corr(lowScoresCol))))

print(f"Correlation between average score and high scores: {correlationHighScores}\nCorrelation between average score and low scores: {correlationLowScores}")

#print(df)

model2 = sm.OLS(lowScoresCol, scoreColumn)
res = model2.fit()
print(res.summary())

X = df.drop(["<5%", "#", "Title", "Controv.", "MainArtist"], axis = 1)
y = df["<5%"]
print(X, y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

results = pd.DataFrame({
    'Actual': y_test,
    'Predicted': model.predict(X_test)
})

print(f"Results here:\n{results}")

mae = mean_absolute_error(y_test, results["Predicted"])
mse = mean_squared_error(y_test, results["Predicted"])
r2 = r2_score(y_test, results["Predicted"])

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'R2: {r2}')
#exit()

plt.subplot(1, 2, 1)
# Selecting the first feature of X_test for plotting against predictions
plt.scatter(X_test.iloc[:, 0], results["Predicted"], color='purple', label='Actual Data')
#plt.plot(X_test[:, 0], predictions, color='blue', linewidth=2, label='Regression Line')
plt.xlabel('X_test (First Feature)')
plt.ylabel('Predictions')
plt.title(f'The model relationship (Scores below 5\n vs average score)')
plt.legend()

# plot for the accuracy
plt.subplot(1, 2, 2)
plt.scatter(y_test, results["Predicted"], color='blue', alpha=0.6)
plt.plot([y_test.min(), results["Predicted"].max()], [y_test.min(), results["Predicted"].max()], 'k--', lw=2, label='Perfect Prediction')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Accuracy of the model')
plt.legend()

plt.tight_layout()
plt.show()


# model = LinearRegression()
# model.fit(scoreColumn.values.reshape(-1, 1), lowScoresCol.values.reshape(-1, 1))
# y_pred = model.predict(scoreColumn.values.reshape(-1, 1))

# mse = mean_squared_error(y_true=lowScoresCol.values.reshape(-1, 1), y_pred=y_pred)
# rmse = root_mean_squared_error(y_true=lowScoresCol.values.reshape(-1, 1), y_pred=y_pred)
# print(f"The mean squared error: {mse}")
# print(f"The root mean squared error: {rmse}")

k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)
kScores = cross_val_score(model, X_test, y_test, cv=kf)
print(f"The scores for each K fold: {kScores}")
print(f"The average K Fold score: {np.mean(kScores)}")

exit()

plt.figure()
plt.scatter(scoreColumn.values.reshape(-1, 1), lowScoresCol, label = "Data", marker = "x", color = "black")
plt.plot(scoreColumn.values.reshape(-1, 1), y_pred, color = "red", label = "Regression line")
plt.xlabel("Average scores")
plt.ylabel("% of scores that are 5 or lower")
plt.ylim(0, 100)
plt.xlim(1, 10)
plt.grid(True)
plt.show()

print(f"Slope coefficient: {model.coef_[0][0]}\nIntercept: {model.intercept_[0]}")

model2 = sm.OLS(lowScoresCol, scoreColumn)
res = model2.fit()
print(res.summary())

#model2 = sm.OLS(formula="Score ~ <5%", data=df).fit()
#print(model2.summary())

#model = LinearRegression()
#model.fit(x, y)