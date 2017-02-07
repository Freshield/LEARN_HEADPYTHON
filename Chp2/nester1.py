"""this is the standard way to
include a multiple-line coment in
your code."""
def print_lol(the_list):
    """name the list"""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
