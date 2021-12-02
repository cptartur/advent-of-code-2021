from itertools import groupby
from operator import itemgetter

with open('in.txt', 'r') as f:
    t = [(x, int(y)) for x, y in map(str.split, f.read().splitlines())]
d = ({k: sum(i[1] for i in list(g)) for k, g in groupby(
    sorted(t, key=lambda x: x[0]), key=itemgetter(0))})
print((d['down'] - d['up']) * d['forward'])
