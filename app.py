# from movie import Movie
# from user import User
# import os
#
# cont = True
#
# m = Movie('avi', 'comedy')
#
# m1 = Movie("akshay", "action")
# m2 = Movie("k3g", "romance")
# m3 = Movie("indian", "action")
#
# u = User("avijatya")
# u.add_movie(m)
# u.add_movie(m1)
#
# print(u.return_movie("akshay"))
#
# u.add_movie(m2)
# u.add_movie(m3)
#
# u.list_all_movies()
#
# print("\n\n")
#
# print(u.get_movies_by_genere('action'))
#
# print(u.play_movie('indian'))
# d = input()
# print(u.play_movie('indian'))
#
# if d == 'd':
#     os.unlink('avijatya')

def unpacking(name, age):
    print("{} and age {} are => ".format(name,age))

d = {'name':'avi','age':30}

unpacking(**d)
