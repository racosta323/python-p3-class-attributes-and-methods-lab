import ipdb

class Song:
    count = 0

    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
      
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += 1

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.genres
    
    @classmethod
    def check_artist(cls,artist):
        return artist in cls.artists

    @classmethod
    def add_to_genres(cls, genre):
        if not genre in cls.genres:
            cls.genres.append(genre)   
   
    @classmethod
    def add_to_artists(cls, artist):
        if not artist in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre, increment =1):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist, increment =1):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1        