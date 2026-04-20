import pandas as pd

df = pd.read_csv("data.csv")
print(df)
print("Average:", df["Marks"].mean())
print("Max:", df["Marks"].max())
print("Min:", df["Marks"].min())
topper = df[df["Marks"] == df["Marks"].max()]
print(topper)
