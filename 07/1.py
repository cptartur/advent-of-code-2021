import math

with open('in.txt', 'r') as f:
    t = [int(i) for i in f.read().split(',')]
lowest = sum(t)
for value in range(min(t), max(t) + 1):
    lowest = min(lowest, sum(math.fabs(value - i) for i in t))
print(lowest)
