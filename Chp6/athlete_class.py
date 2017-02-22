class Athleste:
    def __init__(self, name, dob, times):
        self.name = name
        self.dob = dob
        self.times = times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def add_time(self,time):
        self.times.append(time)

    def add_times(self,times):
        self.times.extend(times)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            data = data.strip().split(',')
            return Athleste(data.pop(0),data.pop(0),data)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

names = ['james','julie','mikey','sarah']

for i in range(4):
    data = get_coach_data(names[i] + '2.txt')
    print(data.name + "'s fastest times are: " + str(data.top3()))

sarah = get_coach_data('sarah2.txt')
sarah.add_time('2.12')
sarah.add_times(['3.23','3.45'])

print(sarah.times)


class AthleteList(list):
    def __init__(self, name, dob, times):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]

    def add_time(self,time):
        self.append(time)

    def add_times(self, times):
        self.extend(times)

def get_coach_data_list(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            data = data.strip().split(',')
            return AthleteList(data.pop(0),data.pop(0),data)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None

for i in range(4):
    data = get_coach_data_list(names[i] + '2.txt')
    print(data.name + "'s fastest times are: " + str(data.top3()))