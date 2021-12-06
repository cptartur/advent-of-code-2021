from collections import Counter

with open('in.txt', 'r') as f:
    t = [int(i) for i in f.read().split(',')]
days = Counter()
days.update(t)
for i in range(256):
    days_new = Counter()
    days_new.update({i: days[i + 1] for i in range(7, -1, -1)})
    days_new.update({8: days[0], 6: days[0]})
    days = days_new
print(sum(days.values()))

# 1687617803407
