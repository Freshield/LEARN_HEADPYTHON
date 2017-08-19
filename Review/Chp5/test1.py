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
        clean_data = sorted([sanitize(item) for item in data])

        unique_list = []
        for item in clean_data:
            if item not in unique_list:
                unique_list.append(item)
        print(clean_data)
        print(unique_list[0:3])
        print()

