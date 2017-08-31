import pickle
from athlete_class import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            data = data.strip().split(',')
            return AthleteList(data.pop(0),data.pop(0),data)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None

def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        ath=get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print 'File error (put and store):' + str(ioerr)
    return all_athletes

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print 'File error (get_from_store):'+str(ioerr)
    return all_athletes

the_files = ['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
data = put_to_store(the_files)
print data

for each in data:
    print data[each].name
    print data[each].dob

data_copy = get_from_store()
print data_copy
