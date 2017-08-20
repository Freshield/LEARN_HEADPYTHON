cleese = {}
palin = dict()
print(type(cleese))
print(type(palin))

cleese['Name'] = 'john clees'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = {'Name':'michael palin', 'Occupations':['comedian', 'actor', 'writer', 'tv']}

print(palin['Name'])

print(cleese['Occupations'][-1])

palin['Birthplace'] = 'broomhill'
cleese['Birthplace'] = 'weston'

print(palin)
print(cleese)