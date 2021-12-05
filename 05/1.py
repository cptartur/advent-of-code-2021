from collections import Counter


with open('in.txt', 'r') as f:
    t = [
        sorted([tuple(map(int, i.split(','))) for i in line.split(' -> ')])
        for line in f.read().splitlines()
    ]
counter = Counter()
for x, y in t:
    if x[1] == y[1]:
        counter.update((i, x[1]) for i in range(x[0], y[0] + 1))
    if x[0] == y[0]:
        counter.update((x[0], i) for i in range(x[1], y[1] + 1))
count = 0
for k, v in counter.items():
    if v >= 2:
        count += 1
print(count)
