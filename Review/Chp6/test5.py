class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

sarah = Athlete('sarah', '2002', ['2:58','2.58','1.56'])
james = Athlete('james')

print(sarah)
print(james)

print(type(sarah))

print(sarah.name)
print(james.name)
print(sarah.dob)
print(james.dob)
print(sarah.times)
print(james.times)