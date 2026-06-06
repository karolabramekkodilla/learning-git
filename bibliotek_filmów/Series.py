class Series():
    def __init__(self, title,  year='unknown', genre='unknown', season_number=1, episode_number=1 , plays_number=0):
        self.title = title
        self.year = year
        self.genere = genre
        self.season_number = season_number
        self.episode_number = episode_number
        self.plays_number = plays_number

    def play(self):
        self.plays_number += 1

    def __str__(self):
        return f"\"{self.title} S{self.season_number:02}E{self.episode_number:02}\""