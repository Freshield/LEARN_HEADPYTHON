"""this is the standard way to
include a multiple-line coment in
your code."""
import sys

def print_lol(the_list, indent=False, level=0, place=sys.stdout):

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,place)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t',end='',file=place)
            print(each_item,file=place)