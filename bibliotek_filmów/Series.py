class Series():
    def __init__(self, title,  year='unknown', genre='unknown', episode_number=1, season_number=1, plays_number=0):
        self.title = title
        self.year = year
        self.genere = genre
        self.genere = episode_number
        self.genere = season_number
        self.plays_number = plays_number

    def play(plays_number):
        plays_number += 1

    def __str__(self):
        print(f"{self.title}")