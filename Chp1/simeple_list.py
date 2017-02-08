movies = ["the holy grail",
          "the life of brian",
          "the meaning of life"]

print(movies[1])

cast = ["cleses",'palin','jones',"idle"]

print(cast)

print(len(cast))

print(cast[1])

cast.append("gilliam")
print(cast)

cast.pop()

print(cast)

cast.extend(["grilliam","chapman"])

print(cast)

cast.remove("chapman")

print(cast)

cast.insert(0,"chapman")

print(cast)

print(movies)

movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)

print(movies)

for each_flick in movies:
    print(each_flick)

count = 0
while count < len(movies):
    print(movies[count])
    count = count + 1


movies = [
    "the holy grail",1975,"terry jones & terry gilliam",91,
    ["graham chapman",
     ["michael palin","john cleese","terry gilliam",'eric idel','terry jones']]
]

print(movies[4][1][3])

print(movies)

for each_item in movies:
    print(each_item)

print(isinstance(movies,list))

for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)


for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

def print_lol(the_list):
    for item in the_list:
        if isinstance(item,list):
            print_lol(item)
        else:
            print(item)

print_lol(movies)