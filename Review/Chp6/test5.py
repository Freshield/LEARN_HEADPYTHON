class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return time_string

        mins, secs = time_string.split(splitter)
        return mins + '.' + secs

    def top3(self):
        return sorted(set([self.sanitize(t) for t in self.times]))[0:3]

    def add_time(self, time):
        self.times.append(time)

    def add_times(self, times):
        self.times.extend(times)




def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            temp = data.strip().split(',')
        return Athlete(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print('File error: ' + str(err))
        return None


sarah = get_coach_data('sarah2.txt')

print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

sarah.add_time('6.66')
print(sarah.times)
sarah.add_times(['8.88','9.99'])
print(sarah.times)

