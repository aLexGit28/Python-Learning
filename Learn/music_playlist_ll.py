class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class MusicPlaylist:
    def __init__(self):
        self.head = None

    # Add a song to the playlist
    def add_song(self, song):

        new_song = Node(song)

        # If playlist is empty
        if self.head is None:
            self.head = new_song

        else:
            current = self.head

            # Move to the last song
            while current.next is not None:
                current = current.next

            # Connect last song to new song
            current.next = new_song

    # Play all songs
    def play_playlist(self):

        if self.head is None:
            print("Playlist is empty")
            return

        print("\n🎧 Now Playing Playlist:\n")

        current = self.head

        while current is not None:
            print("Playing:", current.song)

            current = current.next


# Create playlist object
playlist = MusicPlaylist()


# Add songs
playlist.add_song("Shape of You")
playlist.add_song("Believer")
playlist.add_song("Heat Waves")


# Play playlist
playlist.play_playlist()