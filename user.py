from datetime import datetime


class User:
    given_ids = 0

    def __init__(self, name):
        self.name = name
        self.given_ids += 1
        self._id = self.given_ids
        self.movies = []
        self.play_history = {}

    def add_movie(self, movie):
        self.movies.append(movie)

    def return_movie(self, movie_name):
        temp = list(filter(lambda movie: movie.name != movie_name, self.movies))
        if len(temp) == len(self.movies):
            return '\nWe could not find any movie with name {}'.format(movie_name)
        self.movies = temp

    def list_all_movies(self):
        print("Mvies list is : \n{}".format("\n".join([str(x) for x in self.movies])))

    def get_movies_by_genere(self, genre=''):
        return list(filter(lambda x: x.genre == genre, self.movies))

    def play_movie(self, movie_name):
        if self._filter_movie(movie_name):
            listed = self.play_history.get(movie_name, None)
            with open(self.name, 'a+') as my_file:
                if not listed:
                    my_file.write("Started Watching movie {} at {}\n".format(movie_name, datetime.now()))
                    self.play_history[movie_name] = 'W'
                else:
                    print("in listed")
                    content = my_file.read()
                    found = -1
                    for index, line in enumerate(content):
                        if movie_name in line:
                            found = index
                            break
                    if found > -1:
                        content[index] = "Started Watching movie {} at {}\n".format(movie_name, datetime.now())
                        my_file.truncate(0)
                        my_file.write(content)

                print("Updated movies play history")
        else:
            return '\nWe could not find any movie naming {} in your store'.format(movie_name)

    def _filter_movie(self, movie_name=''):
        if movie_name:
            a = [x for x in self.movies if x.name == movie_name]
            return a[0] if len(a) > 0 else None
