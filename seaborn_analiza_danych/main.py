import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

# Wczytanie danych

df = pd.read_csv("HRDataset.csv")

# Zamiana dat
df["DateofHire"] = pd.to_datetime(df["DateofHire"])

# Staż pracy (lata)
df["Seniority"] = (
    pd.Timestamp.today() - df["DateofHire"]
).dt.days / 365

# 1. Manager vs PerformanceScore

plt.figure(figsize=(15,6))

sns.countplot(
    data=df,
    x="ManagerName",
    hue="PerformanceScore"
)

plt.xticks(rotation=90)
plt.title("Performance Score według Managera")
plt.tight_layout()

print("\nPerformanceScore wg Managera")
print(pd.crosstab(df["ManagerName"], df["PerformanceScore"]))

# 2. Recruitment Source vs Seniority

plt.figure(figsize=(12,6))

sns.boxplot(
    data=df,
    x="RecruitmentSource",
    y="Seniority"
)

plt.xticks(rotation=45)
plt.title("Źródło rekrutacji a staż pracy")
plt.tight_layout()

print("\nŚredni staż wg źródła rekrutacji")
print(
    df.groupby("RecruitmentSource")["Seniority"]
      .mean()
      .sort_values(ascending=False)
)

# 3. Marital Status vs Satisfaction

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="MaritalDesc",
    y="EmpSatisfaction"
)

plt.title("Stan cywilny a satysfakcja z pracy")

print("\nŚrednia satysfakcja")
print(
    df.groupby("MaritalDesc")["EmpSatisfaction"]
      .mean()
)

# 4. Struktura wieku
# print(df["DOB"].head(10))
df["DOB"] = pd.to_datetime(df["DOB"], format="%m/%d/%y")

df.loc[df["DOB"] > pd.Timestamp.today(), "DOB"] -= pd.DateOffset(years=100)


today = pd.Timestamp.today()

df["Age"] = (
    today.year
    - df["DOB"].dt.year
    - (
        (today.month < df["DOB"].dt.month)
        | (
            (today.month == df["DOB"].dt.month)
            & (today.day < df["DOB"].dt.day)
        )
    )
)
plt.figure(figsize=(10,6))

sns.histplot(
    data=df,
    x="Age",
    bins=20,
    kde=True
)

plt.title("Struktura wieku pracowników")

print("\nOpis wieku")
print(df["Age"].describe())

# 5. Age vs SpecialProjectsCount


sns.lmplot(
    data=df,
    x="Age",
    y="SpecialProjectsCount",
    height=6,
    aspect=1.5
)

plt.title("Wiek a liczba projektów")

print("\nKorelacja")
print(
    df[["Age", "SpecialProjectsCount"]].corr()
)

plt.show()