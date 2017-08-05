def print_list(the_list):
    for each_item in the_list:
        if isinstance(each_item,list) == True:
            print_list(each_item)
        else:
            print(each_item)

movies = [
    'the holy grail', 1975, 'terry jones & terry filliam', 91,
    ['graham chapman',
     ['michsel palin', 'john cleese','terry filliam','eric idle','terry jones']]
]

print_list(movies)