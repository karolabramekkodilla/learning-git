import pandas as pd
import requests
from io import StringIO

url = "https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
print(response.status_code)
html = response.text
data = pd.read_html(StringIO(html), header=0)[0]

data.rename(columns={'TITLE':'TYTUŁ','ARTIST':'ARTYSTA','YEAR':'ROK','HIGH POSN':'MAX POZ'},inplace = True)
print("\nTabela po zmianie nazw kolumn:")
print(data)

unq_artist = data["ARTYSTA"].nunique()
print(f"Pojedynczych artystów na liście = {unq_artist}")
unq_artist_list = data["ARTYSTA"].value_counts().head(5)
print("\nPięciu najczęściej występujących artystów:")
print(unq_artist_list)
data.columns = data.columns.str.capitalize()
print("\nTabela po zmianie wielkości liter w nazwach kolumn:")
print(data)
data.drop('Max poz',axis = 1,inplace = True)
print("\nTabela po usunięciu kolumny 'Max poz':")
print(data)
years_list = data["Rok"].value_counts().head(1)
print("\nNajczęściej występujący rok wydania:")
print(years_list)

years_list_between = data[(data['Rok'].between(1960,1990))]
print("\nAlbumy wydane w latach 1960–1990:")
print(years_list_between)

print(f"Najmłodszy album został wydany w {data['Rok'].max()} roku.")

first_album_list = data.loc[data.groupby("Artysta")["Rok"].idxmin()]
print("\nNajwcześniej wydany album każdego artysty:")
print(first_album_list)

try:
    first_album_list.to_csv("first_album_list.csv", index=False)
    print("\nLista została zapisana do pliku first_album_list.csv")
except OSError as e:
    print(f"\nNie udało się zapisać pliku: {e}")



