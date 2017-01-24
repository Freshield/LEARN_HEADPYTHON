with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)

the_list = [james,julie,mikey,sarah]

data = [6,3,1,2,4,5]
print(data)
data.sort()
print(data)

data = [6,3,1,2,4,5]
print(data)
data2 = sorted(data)
print(data)
print(data2)

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)

    return (mins + '.' + secs)

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))

for each_t in julie:
    clean_julie.append(sanitize(each_t))

for each_t in mikey:
    clean_mikey.append(sanitize(each_t))

for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

mins = [1,2,3]
secs = [m * 60 for m in mins]
print(secs)

meters = [1,10,3]
feet = [m * 3.281 for m in meters if m > 2]
print(feet)

lower = ['I',"don't",'like','spam']
upper = [s.upper() for s in lower]
print(upper)

dirty = ['2-22','2:22','2.22']
clean = [sanitize(t) for t in dirty]
print(clean)

clean = [float(s) for s in clean]
print(clean)

clean = [float(sanitize(t)) for t in ['2-22','3:33','4.44']]
print(clean)

for i,item in enumerate(the_list):
    the_list[i] = sorted([sanitize(t) for t in item])

for item in the_list:
    print(item)


ujames = []
ujulie = []
umikey = []
usarah = []
unique = [ujames,ujulie,umikey,usarah]
for item in range(0,len(the_list)):
    for each_t in the_list[item]:
        if each_t not in unique[item]:
            unique[item].append(each_t)

for item in unique:
    print(item[0:3])

distance = set()
distance = {10.6,11,8,10.6,'two',7}

print(distance)

distance = set(james)
print(distance)

the_result = []
for item in the_list:
    the_result.append(sorted(set([sanitize(t) for t in item])))

for item in the_result:
    print(item[0:3])

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as err:
        print('file error ' + str(err))
        return None

data_list = []
file_list = ['james.txt','julie.txt','mikey.txt','sarah.txt']
fast_list = []

data_list = [get_coach_data(t) for t in file_list]

fast_list = sorted(set([sanitize(t) for t in item] for item in data_list))[0:3]

for item in fast_list:
    print(item)