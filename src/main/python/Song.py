from src.main.python.SongComponent import SongComponenet

class Song(SongComponenet):

    def __init__(self, name, band):
        self.name = name
        self.band = band

    def get_name(self):
        return self.name

    def get_band(self):
        return self.band

    def display(self):
        print(self.get_name() + " released by " + self.get_band())