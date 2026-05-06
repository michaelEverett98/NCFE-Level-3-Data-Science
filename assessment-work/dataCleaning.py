import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
#pd.set_option("display.max_rows", None)

df = pd.read_csv("randomStats.csv")

df['Height'] = df["Height"].astype(float)

df = df.drop_duplicates(subset = ["Weight"])

averageHeight = df["Height"].mean()

df = df.fillna(averageHeight)

print(df) 