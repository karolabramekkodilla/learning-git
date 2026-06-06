from Movie import Movie
from Series import Series
import random
from datetime import date

def get_movies(library):
    pass
def get_series(library):
    pass
def search(library):
    pass
def generate_views(library):
    for item in library:
        item.plays_number += random.randint(1,100)

def top_titles(library, content_type):
    pass

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
date = date.today().strftime("%d.%m.%Y")
print(f"Najpopularniejsze filmy i seriale dnia {date}")