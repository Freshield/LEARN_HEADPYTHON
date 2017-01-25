import sys, pickle

man = []
other = []

def print_lol(the_list, indent=False, level=0, place=sys.stdout):

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,place)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t',end='',file=place)
            print(each_item,file=place)

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('the datafile is missing')

try:
    with open('man_data.txt','wb') as man_file, open('other_data.txt','wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('file error: ' + str(err))
except pickle.PickleError as perr:
    print('pickling error: ' + str(perr))

import nester

new_man = []

try:
    with open('man_data.txt','rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('file error: ' + str(err))
except pickle.PickleError as perr:
    print('pickling error: ' + str(err))

nester.print_lol(new_man)

print(new_man[0])

print(new_man[-1])



