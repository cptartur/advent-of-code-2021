from math import fabs, floor

with open('in.txt', 'r') as f:
    t = [int(i) for i in f.read().split(',')]
lowest = sum(i for value in t for i in range(value + 1))
for v in range(min(t), max(t) + 1):
    lowest = min(lowest, sum(
        i for value in t for i in range(floor(fabs(v - value)) + 1)))
print(lowest)
