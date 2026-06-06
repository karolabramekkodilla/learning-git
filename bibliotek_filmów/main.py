from Movie import Movie
from Series import Series
import random
from datetime import date

def get_movies(library):
    movies = []
    for item in library:
        if isinstance(item,Movie):
            movies.append(item)
    movies.sort(key= lambda movie: movie.title)
    return movies
def get_series(library):
    series = []
    for item in library:
        if isinstance(item,Series):
            series.append(item)
    series.sort(key= lambda series: series.title)
    return series
def search(title,library):
    for item in library:
        if item.title == title:
            return item
    return None
def generate_views(library):    
        item = random.choice(library)
        item.plays_number += random.randint(1,100)

def top_titles(library, content_type):
    if content_type == "series":
        series = get_series(library)
        series.sort(key=lambda series: series.plays_number, reverse = True)
        return series[0:3]
    elif content_type == "movies":
        movies = get_movies(library)
        movies.sort(key=lambda movie: movie.plays_number, reverse = True)
        return movies[0:3]
    else:
        return f"Nieprawidłowy content type"
    
def generate_views_ten_times(library):
    for i in range(10):
        generate_views(library)

print("Biblioteka filmów")
# lista na filmy i seriale
library = [
    Movie("Pulp Fiction", 1994, "Crime"),
    Movie("Matrix", 1999, "Sci-Fi"),
    Movie("The Green Mile", 1999, "Drama"),
    Movie("Inception", 2010, "Sci-Fi"),
    Movie("Gladiator", 2000, "Historical"),
    Movie("Interstellar", 2014, "Sci-Fi"),

    Series("Breaking Bad", 2008, "Crime Drama", 1, 1),
    Series("Breaking Bad", 2008, "Crime Drama", 1, 2),
    Series("Breaking Bad", 2008, "Crime Drama", 1, 3),

    Series("Friends", 1994, "Comedy", 1, 1),
    Series("Friends", 1994, "Comedy", 1, 2),
    Series("Friends", 1994, "Comedy", 1, 3),

    Series("The Simpsons", 1989, "Comedy", 1, 1),
    Series("The Simpsons", 1989, "Comedy", 1, 2),
    Series("The Simpsons", 1989, "Comedy", 2, 1),

    Series("House M.D.", 2004, "Medical Drama", 1, 1),
    Series("House M.D.", 2004, "Medical Drama", 2, 1),

]

generate_views(library)
generate_views_ten_times(library)
date = date.today().strftime("%d.%m.%Y")
print(f"Najpopularniejsze filmy i seriale dnia {date}")
top_series = top_titles(library, "series")
top_movies = top_titles(library, "movies")
i=1
for movie in top_movies:
    
    print(f"Film nr{i} to {movie}")
    i+=1
i=1
for series in top_series:
    
    print(f"Serial nr{i} to {series}")
    i+=1