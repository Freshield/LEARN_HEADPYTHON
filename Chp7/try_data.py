cleese = {}
palin = dict()
print(type(cleese))
print(type(palin))

cleese['Name'] = "john cleese"
cleese['Occupations'] = ['actor','comedian','writer','film producer']
palin = {'Name':'michael palin','Occupations':['comedian','actor','writer','tv']}
print(palin['Name'])
print(cleese['Occupations'][-1])

palin['Birthplace'] = "broomhill,sheffield,england"
cleese['Birthplace'] = 'weston-super-mare,north somerset,england'

print(palin)
print(cleese)

class Athlete:
    def __init__(self, value=0):
        print('init')
        self.thing = value
    def how_big(self):
        return len(self.thing)

a = Athlete()

d = Athlete('holy grail')
print(d.how_big())