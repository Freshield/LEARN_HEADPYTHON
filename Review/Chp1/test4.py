movies = ['the holy grail',
          'the life of brian',
          'the meaning of life']

movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)

print(movies)

fav_movies = ['the holy grail', 'the life of brian']

print(fav_movies[0])
print(fav_movies[1])

print()

for each_flick in fav_movies:
    print(each_flick)


print()
count = 0

while count < len(fav_movies):
    print(fav_movies[count])
    count += 1