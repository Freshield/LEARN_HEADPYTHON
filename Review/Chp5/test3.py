mins = [1,2,3]
secs = [m * 60 for m in mins]
print(secs)

meters = [1,10,3]
feets = [m * 3.281 for m in meters]
print(feets)

lower = ['I', "don't", 'like', 'span']
upper = [s.upper() for s in lower]
print(upper)

clean = [float(t) for t in ['2.22','3.33','4.44']]
print(clean)