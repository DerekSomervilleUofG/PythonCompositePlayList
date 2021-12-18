import os
from src.main.python.PlayList import PlayList
from src.main.python.Song import Song

class SongGenerator:

    def get_song(self, song_path):
        bandAndSong = song_path.split(".")[0].split(" - ");
        return Song(bandAndSong[1], bandAndSong[0])

    def navigate_directory(self, music_directory):
        play_list = PlayList(music_directory.split("/")[-1]);
        current_directory = os.getcwd()
        os.chdir(music_directory)
        for musicFile in os.listdir():
            if os.path.isfile(musicFile):
                play_list.add(self.get_song(musicFile.split("/")[-1]))
            elif os.path.isdir(musicFile):
                song_component = self.navigate_directory(musicFile);
                play_list.add(song_component)
        os.chdir(current_directory)
        return play_list


    def generate(self):
        return self.navigate_directory("src/main/resources/Music/")


    def main(self):
        play_list = self.generate()
        play_list.display()

if __name__ == '__main__':
    song_generator = SongGenerator()
    song_generator.main()
