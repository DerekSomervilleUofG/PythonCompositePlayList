class SongComponentIterator:

    def __init__(self, song_components):
        self.song_components = song_components
        self.position = 0

    def has_next(self):
        return self.position < len(self.song_components)

    def next(self):
        song = self.song_components[self.position]
        self.position += 1
        return song