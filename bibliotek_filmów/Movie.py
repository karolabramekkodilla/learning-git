class Movie():
    def __init__(self, title, year='unknown', genre='unknown', plays_number=0):
        self.title = title
        self.year = year
        self.genere = genre
        self.plays_number = plays_number

    def play(self):
        self.plays_number += 1