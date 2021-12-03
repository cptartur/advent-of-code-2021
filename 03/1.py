from collections import Counter


c = Counter()
with open('in.txt', 'r') as f:
    t = [i for i in list(map(list, f.read().splitlines()))]
    t = [list(map(lambda kv: kv[0] if kv[1] == '1' else None, enumerate(entry))) for entry in t]
    c = Counter(x for i in t for x in set(i) if x is not None)
gamma_rate = "".join('1' if v > len(t) - v else '0' for k, v in sorted(c.items()))
epsilon_rate = "".join('0' if v > len(t) - v else '1' for k, v in sorted(c.items()))
print(int(gamma_rate, 2) * int(epsilon_rate, 2))