from itertools import groupby
from operator import itemgetter
from functools import reduce

with open('in.txt', 'r') as f:
    t = [(int(y), 0, 0) if x == 'forward' else (0, 0, int(y)) if x == 'down' else (
        0, 0, -int(y)) for x, y in map(str.split, f.read().splitlines())]
    for i, (x, y, z) in enumerate(t[1:], start=1):
        aim = t[i - 1][2]
        t[i] = (x, y, z + aim) if x == 0 else (x, x * aim, aim)
    
t = [sum(i) for i in zip(*t)]
print(t[0] * t[1])
