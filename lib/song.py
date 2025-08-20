# lib/song.py

class Song:
    # class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # update total count
        Song.count += 1

        # add genre if new
        if genre not in Song.genres:
            Song.genres.append(genre)

        # add artist if new
        if artist not in Song.artists:
            Song.artists.append(artist)

        # update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
