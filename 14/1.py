from collections import Counter

with open('in.txt', 'r') as f:
    template = next(f).strip()
    next(f)
    t = [i.split(' -> ') for i in f.read().splitlines()]

recepies = {i[0]: i[1] for i in t}
count = Counter(template[i : i + 2] for i in range(len(template) - 1))
letters_count = Counter()
last = list(count.keys())[-1]
print(last)

for _ in range(10):
    new_count = Counter()
    for pair, count in count.items():
        new_count[pair[0] + recepies[pair]] += count
        new_count[recepies[pair] + pair[1]] += count
    count = new_count
    last = recepies[last] + last[1]

res = Counter()
for pair, count in count.items():
    res[pair[0]] += count
res[last[1]] += 1

print(res.most_common()[0][1] - res.most_common()[-1][1])
