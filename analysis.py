import pandas as pd

df = pd.read_csv("data.csv")
print(df)

print("Average:", df["Marks"].mean())
print("Max:", df["Marks"].max())
print("Min:", df["Marks"].min())

topper = df[df["Marks"] == df["Marks"].max()]
print(topper)

topper = df[df["Marks"] == df["Marks"].max()]
print(topper)

low_attendance = df[df["Attendance"] < 75]
print(low_attendance)

def grade(m):
    if m >= 80: return "A"
    elif m >= 60: return "B"
    else: return "C"

df["Grade"] = df["Marks"].apply(grade)
print(df)

print(df.sort_values(by="Marks", ascending=False))

print(df.groupby("Subject")["Marks"].mean())
