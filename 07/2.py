from io import open_code
from math import fabs


def progression_sum(n: int) -> int:
    return (1 + n) / 2 * n


with open('in.txt', 'r') as f:
    t = [int(i) for i in f.read().split(',')]
lowest = sum(i for value in t for i in range(value + 1))
for v in range(min(t), max(t) + 1):
    lowest = min(lowest, sum(
        map(progression_sum, (fabs(v - value) for value in t))))
print(lowest)
