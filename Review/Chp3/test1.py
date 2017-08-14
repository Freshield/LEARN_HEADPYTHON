data = open('sketch1.txt')

each_line = data.readline()

role, line_spoken = each_line.split(':')

print(role)

print(line_spoken)