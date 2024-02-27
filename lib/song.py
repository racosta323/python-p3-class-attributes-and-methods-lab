import ipdb

class Song:
    count = 0

    genres = []
    artists = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.artists.append(artist)
        self.add_to_genres(genre)
        self.add_song_to_count()
        # self.add_to_genre_count()

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.genres
    
    @classmethod
    def check_artist(cls,artist):
        return artist in cls.artists
    
    @classmethod
    def add_to_genres(cls, genre):
        if not cls.check_genre(genre):
            cls.genres.append(genre)
            ipdb.set_trace()
            cls.add_to_genre_count()
        else:
            ipdb.set_trace()
            cls.add_to_genre_count()

    @classmethod
    def add_to_artists(cls, artist):
        if not cls.check_artist(artist):
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, increment =1):
        ipdb.set_trace()
        for genre in cls.genres:
            ipdb.set_trace()
            if genre in cls.genre_count:
                ipdb.set_trace()
                cls.genre_count.update({genre: cls.genre_count[genre] + increment})
                ipdb.set_trace()
            else:
                ipdb.set_trace()
                cls.genre_count[genre] = increment


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
other_song = Song("99 Problems", "Jay-Z", "Rock")
another_song = Song("99 Problems", "Jay-Z", "Rock")
# # print(Song.count)
# # # Song.add_to_genres("Rap")
# Song.add_to_genre_count()
