data = open('sketch1.txt')

for line in data:
    if line.find(':') != -1:
        role, line_spoken = line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')

data.close()