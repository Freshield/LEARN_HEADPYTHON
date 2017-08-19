dic = {'ja':'james.txt', 'ju':'julie.txt', 'mi':'mikey.txt', 'sa':'sarah.txt'}

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    mins, secs = time_string.split(splitter)
    return mins + '.' + secs

for key,value in dic.items():
    with open(value) as file:
        data = file.readline()
        data = data.strip().split(',')
        clean_data = [sanitize(item) for item in data]
        print(sorted(clean_data))

