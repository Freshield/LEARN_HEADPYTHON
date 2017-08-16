import sys

man = []
other = []

"""
This is nester.py module
"""
def print_lol(the_list, indent=False, level=0, pos=sys.stdout):
    """
    :param the_list: it can be any python list
    :return:
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, pos)
        else:
            if indent == True:
                """
                for tab_stop in range(level):
                    print('\t',end='')
                """
                print('\t' * level, end='', file=pos)
            print(each_item, file=pos)



try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            role, line_spoken = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError as err:
    print('The datafile is missing!' + str(err))


try:
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        print_lol(man, False, 0, man_file)
        print_lol(other, False, 0, other_file)
except IOError as err:
    print('File error ' + str(err))