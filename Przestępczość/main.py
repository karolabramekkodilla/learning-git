import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fatal-police-shootings-data.csv")
print(df.head())
print(df.info())

print(df["race"].unique())
print(df["signs_of_mental_illness"].unique())
print(df["threat_level"].unique())

table = df.groupby(
    ["race", "signs_of_mental_illness"]
).size().unstack(fill_value=0)

print(table)

def calculate_mental_illness_percentage(row):
    return row[True] / (row[True] + row[False]) * 100

table["percent"] = table.apply(calculate_mental_illness_percentage, axis=1)
print(table)

df["date"] = pd.to_datetime(df["date"])

df["weekday"] = df["date"].dt.day_name()
print(df)
interventions_by_day = df["weekday"].value_counts()

days_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

interventions_by_day = interventions_by_day.reindex(days_order)

print(interventions_by_day)

interventions_by_day.plot(kind="bar")

plt.title("Liczba interwencji według dnia tygodnia")
plt.xlabel("Dzień tygodnia")
plt.ylabel("Liczba interwencji")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()