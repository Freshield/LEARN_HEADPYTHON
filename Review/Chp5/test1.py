dic = {'ja':'james.txt', 'ju':'julie.txt', 'mi':'mikey.txt', 'sa':'sarah.txt'}

for key,value in dic.items():
    with open(value) as file:
        data = file.readline()
        data = data.strip().split(',')
        print(data)
