from src.main.python.SongComponent import SongComponenet
from src.main.python.SongComponentIterator import SongComponentIterator

class PlayList(SongComponenet):

    def __init__(self, name):
        self.name = name
        self.song_componenets = []

    def get_name(self):
        return self.name

    def add(self, song_componenet):
        self.song_componenets.append(song_componenet)

    def display(self):
        print(self.get_name())
        song_iterator = SongComponentIterator(self.song_componenets)
        while song_iterator.has_next():
            song_iterator.next().display()