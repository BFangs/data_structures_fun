from queues import Queue
# designing a jukebox

# list of songs
# way to select song
#     play song
# cds
# cd player
# playlist queue


class Jukebox(object):
    def __init__(self):
        self.collection = set()
        self.playlist = Queue()

    def display_songs(self):

    def select_song(self, id):

    def play_song(self):


class CDPlayer(object):
    def __init__(self):
        self.curr = None


class Song(object):
    def __init__(self, title, length, CD):
        self.title = title
        self.length = length
        self.CD = CD

class CD(object):
    def __init__(self, title, artist, songs=[]):
        self.title = title
        self.artist = artist
        self.songs = songs