import os

print(os.getcwd())

try:
    data = open('sketch.txt')

    print(data.readline(),end='')
    print(data.readline(),end='')

    data.seek(0)

    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            print(role,end='')
            print(' said: ',end='')
            print(line_spoken,end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('not find file')
