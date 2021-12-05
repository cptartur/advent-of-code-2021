import math
from collections import Counter


with open('in.txt', 'r') as f:
    t = [sorted([tuple(map(int, i.split(','))) for i in line.split(' -> ')])
         for line in f.read().splitlines()]
counter = Counter()
for x, y in t:
    if x[1] == y[1]:
        counter.update((i, x[1]) for i in range(x[0], y[0] + 1))
    if x[0] == y[0]:
        counter.update((x[0], i) for i in range(x[1], y[1] + 1))
    if math.fabs(dx := y[0] - x[0]) == math.fabs(dy := y[1] - x[1]):
        x_sign = 1 if dx >= 0 else -1
        y_sign = 1 if dy >= 0 else -1
        counter.update((i, j) for i, j in zip(
            range(x[0], y[0] + x_sign, x_sign), range(x[1], y[1] + y_sign, y_sign)))
count = 0
for k, v in counter.items():
    if v >= 2:
        count += 1
print(count)
