import os

print(os.getcwd())

data = open('sketch1.txt')

print(data.readline(), end='')

print(data.readline(), end='')

data.seek(0)

for each_line in  data:
    role, line_spoken = each_line.split(':',1)
    print(role,end='')
    print(' said: ',end='')
    print(line_spoken, end='')

data.close()