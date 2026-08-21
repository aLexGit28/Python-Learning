class MusicPlaylist:

    def __init__(self):
        self.playlist = []

    # Add a song to the playlist
    def add_song(self, song):
        self.playlist.append(song)
        print(song, "added to the playlist.")

    # Play and remove the oldest song
    def play_song(self):
        if self.is_empty():
            print("Playlist is empty!")
        else:
            song = self.playlist.pop(0)
            print("Now playing:", song)

    # Show all songs in the playlist
    def show_playlist(self):
        if self.is_empty():
            print("Playlist is empty!")
        else:
            print("\nSongs in the playlist:")
            for song in self.playlist:
                print("-", song)

    # Check whether the playlist is empty
    def is_empty(self):
        return len(self.playlist) == 0