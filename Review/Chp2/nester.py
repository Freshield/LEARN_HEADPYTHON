"""
This is nester.py module
"""
def print_lol(the_list, indent=False, level=0):
    """
    :param the_list: it can be any python list
    :return:
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent == True:
                """
                for tab_stop in range(level):
                    print('\t',end='')
                """
                print('\t' * level, end='')
            print(each_item)

