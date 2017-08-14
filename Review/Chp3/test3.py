try:
    data = open('sketch1.txt')

    for line in data:
        try:
            role, line_spoken = line.split(':',1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except ValueError:
    print('value error')
except IOError:
    print('io error')
except:
    print('other error')