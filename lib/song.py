import ipdb

class Song:
    count = 0

    genres = []
    artists = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        # self.genre = genre
        if self.check_genre(genre):
            self.genre = genre     
        else:
            self.genres.append(genre)
        self.add_song_to_count()
        self.add_to_genre_count()
        self.artists.append(artist)
        
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
    def add_to_artists(cls, artist):
        if not cls.check_artist(artist):
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, increment =1):
        for genre in cls.genres:
            if genre in cls.genre_count:
                cls.genre_count[genre] +=1
            else:
                cls.genre_count[genre] = 1
    

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
other_song = Song("99 Problems", "Jay-Z", "Rock")
another_song = Song("99 Problems", "Jay-Z", "Rock")
print(Song.genre_count)
# # print(Song.count)
# # # Song.add_to_genres("Rap")
# Song.add_to_genre_count()
