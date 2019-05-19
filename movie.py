class Movie:

    def __init__(self, name, genre, director=None, cast={}, release_date=None):
        self.name = name
        self.genre = genre
        self.duration = 90

    def __repr__(self):
        return "{} is the movie of genre {}".format(self.name, self.genre)


