def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            data = data.strip().split(',')

            dir = {}
            dir['Name'] = data.pop(0)
            dir['Dob'] = data.pop(0)
            dir['Times'] = data
            dir['Fast'] = sorted(set([sanitize(t) for t in dir['Times']]))[0:3]

        return dir
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None

sarah = get_coach_data('sarah2.txt')
"""
#(sarah_name, sarah_dob) = (sarah.pop(0),sarah.pop(0))
#print(sarah_name + "'s fastest times are: "+
#      str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

sarah_dir = {}
sarah_dir['Name'] = sarah.pop(0)
sarah_dir['Dob'] = sarah.pop(0)
sarah_dir['Times'] = sarah

james = get_coach_data('james2.txt')

print(james['Name'] + "'s fastest times are: " + str(james['Fast']))
"""
names = ['james','julie','mikey','sarah']

for i in range(4):
    data = get_coach_data(names[i] + '2.txt')
    print(data['Name'] + "'s fastest times are: " + str(data['Fast']))

