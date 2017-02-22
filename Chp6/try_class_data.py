class Athlete:
    def __init__(self, name, dob=None, times = []):
        self.name = name
        self.dob = dob
        self.times = times

sarah = Athlete('sarah','2002-6-17',['2.58','2.58','1.56'])
print(type(sarah))
print(sarah)
print(sarah.name)
print(sarah.dob)
print(sarah.times)

class NamedList(list):
    def __init__(self,name):
        list.__init__([])
        self.name = name

johnny = NamedList('john')
print(type(johnny))
print(dir(johnny))

johnny.append('bass')
johnny.extend(['composer','arranger','musician'])
print(johnny)
print(johnny.name)

for attr in johnny:
    print(johnny.name + ' is a ' + attr)

d = {}
d['size'] = 10
print(d)
d = {'name':'lol'}
print(d)