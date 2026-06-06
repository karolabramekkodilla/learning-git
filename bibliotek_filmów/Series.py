class Series():
    def __init__(self, title,  year='unknown', genre='unknown', episode_number=1, season_number=1, plays_number=0):
        self.title = title
        self.year = year
        self.genere = genre
        self.episode_number = episode_number
        self.season_number = season_number
        self.plays_number = plays_number

    def play(plays_number):
        plays_number += 1

    def __str__(self):
        return f"\"{self.title} S{self.season_number:02}E{self.episode_number:02}\""