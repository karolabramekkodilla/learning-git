import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Punkt 1
df_gen = pd.read_csv('tmdb_genres.csv')
df_mov = pd.read_csv('tmdb_movies.csv')
print(df_gen.head())
print(df_mov.head())

q3 = df_mov['vote_count'].quantile(0.75)
print(f"Trzeci kwartyl liczby głosów: {q3}")
print(q3)
temp = df_mov[df_mov['vote_count'] > q3]
print(temp.head(10))
top10 = (temp.sort_values('vote_average',ascending=False).head(10))
print(top10)
# Punkt drugi
df_mov["release_date"] = pd.to_datetime(df_mov["release_date"])
df_mov["year"] = df_mov["release_date"].dt.year
movies = df_mov[
    (df_mov["year"] >= 2010) &
    (df_mov["year"] <= 2016)
]
result = movies.groupby("year")
result = result[["revenue", "budget"]].mean()

fig, ax = plt.subplots()

ax.bar(result.index, result["revenue"], label="Revenue")

ax.plot(result.index, result["budget"],
        marker="o",
        label="Budget")
ax.set_title("Average revenue and budget (2010-2016)")
ax.set_xlabel("Year")
ax.set_ylabel("USD")
ax.legend(loc="upper left",
          bbox_to_anchor=(1.02, 1))
plt.tight_layout()
plt.show()

# Punkt trzeci
print(df_gen.head())
print(df_mov.head())
df_gen = df_gen.rename(columns={"Unnamed: 0": "genre_id"})
df_mov = pd.merge(df_mov, df_gen, on="genre_id")
print(df_mov.head())

# Punkt czwarty

genre_count = df_mov["genres"].value_counts()

most_common_genre = genre_count.index[0]
number_of_movies = genre_count.iloc[0]

print(f"Najczęstszy gatunek: {most_common_genre}")
print(f"Liczba filmów: {number_of_movies}")

# Punkt piąty

runtime_by_genre = (
    df_mov
    .groupby("genres")["runtime"]
    .mean()
    .sort_values(ascending=False)
)

print(runtime_by_genre.head(1))

# Punkt szósty
runtime_by_genre = (
    df_mov
    .groupby("genres")["runtime"]
    .mean()
    .sort_values(ascending=False)
)

longest_genre = runtime_by_genre.index[0]

genre_movies = df_mov[df_mov["genres"] == longest_genre]

plt.hist(genre_movies["runtime"])
plt.title(f"Runtime of {longest_genre} movies")
plt.xlabel("Runtime [min]")
plt.ylabel("Number of movies")
plt.show()