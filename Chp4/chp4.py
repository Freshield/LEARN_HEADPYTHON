man = []
other = []

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

print(man)
print(other)

out = open('data.out','w')
print('norwegian blues stun easily.',file=out)
out.close()

try:
    manWords = open('man_data.txt','w')
    otherWords = open('other_data.txt','w')

    print(man,file=manWords)
    print(other,file=otherWords)

except IOError:
    print('file error')
finally:
    if ('manWords' in locals()) and ('otherWords' in locals()):
        manWords.close()
        otherWords.close()

