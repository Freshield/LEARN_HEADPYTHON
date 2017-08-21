class NamedList(list):
    def __init__(self,name):
        list.__init__([])
        self.name = name

johnny = NamedList('john')
print(type(johnny))

print(dir(johnny))

print(johnny)
print(johnny.name)