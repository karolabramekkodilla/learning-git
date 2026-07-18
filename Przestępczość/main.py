import pandas as pd
import matplotlib.pyplot as plt
import requests
import time
from io import StringIO


# 1
df = pd.read_csv("fatal-police-shootings-data.csv")
print("Pobrana tabela fatal-police-shootings-data")
print(df.head())
# print(df.info())
print()

# 2

# print(df["race"].unique())
# print(df["signs_of_mental_illness"].unique())
# print(df["threat_level"].unique())

table = df.groupby(
    ["race", "signs_of_mental_illness"]
).size().unstack(fill_value=0)
print("Tabela zestawiająca race oraz signs_of_mental_illness")
print(table)
print()

# 3
def calculate_mental_illness_percentage(row):
    return row[True] / (row[True] + row[False]) * 100

table["percent"] = table.apply(calculate_mental_illness_percentage, axis=1)
print(table)
best_row = table.sort_values("percent", ascending=False).iloc[0]
print(f"Największym odsetkiem znamion choroby psychicznej podczas interwencji jest : {best_row.name}")
print()


# 4
df["date"] = pd.to_datetime(df["date"])

df["weekday"] = df["date"].dt.day_name()
print("Kolumna z dniami tygodnia dla interwencji")
print(df)
print()
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
print("Interwencje wg dnia tygodnia")
print(interventions_by_day)
print()

interventions_by_day.plot(kind="bar")

plt.title("Liczba interwencji według dnia tygodnia")
plt.xlabel("Dzień tygodnia")
plt.ylabel("Liczba interwencji")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5
url1 = "https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population"
url2 = "https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations"

headers = {
    "User-Agent": "Kodilla/1.0"
}

response1 = requests.get(url1, headers=headers)
print(response1.status_code)
html1 = response1.text
# print(html)
data1 = pd.read_html(StringIO(html1), header=0)[0]
print(data1.columns.tolist())
# print(data1)
time.sleep(2)
response2 = requests.get(url2, headers=headers)
print(response2.status_code)
html2 = response2.text
data2 = pd.read_html(StringIO(html2), header=0)[1]
print(data2.columns.tolist())
# print(data2)

population = pd.merge(data1, data2, left_on="State", right_on="Name")
population = population[["USPS (& ANSI)", "Census population, April 1, 2020 [1][2]"]]
population["Census population, April 1, 2020 [1][2]"] = population["Census population, April 1, 2020 [1][2]"] / 1000
# print(population)

incidents = df["state"].value_counts().reset_index()
incidents.columns = ["state", "incidents"]
# print(incidents)

result = pd.merge(incidents,population,left_on="state",right_on="USPS (& ANSI)")
result["incidents_per_1000"] = (result["incidents"] / result["Census population, April 1, 2020 [1][2]"])
result.sort_values("incidents_per_1000", ascending=False, inplace=True)
print(result)