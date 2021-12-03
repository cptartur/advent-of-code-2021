from collections import Counter
from types import FunctionType


def rating(t: list, position: int, f: FunctionType) -> list:
    if (len(t)) == 1:
        return "".join(t[0])
    t1 = t.copy()
    t1 = [list(map(lambda kv: kv[0] if kv[1] == '1' else None,
               enumerate(entry))) for entry in t]
    c = Counter(x for i in t1 for x in set(i) if x is not None)
    most_common = f(c, position, len(t))
    t = list(filter(lambda entry: entry[position] == most_common, t))
    return rating(t, position + 1, f)


c = Counter()
with open('in.txt', 'r') as f:
    t = [i for i in list(map(list, f.read().splitlines()))]

t1 = t.copy()
oxygen_rating = rating(t.copy(), 0, lambda c,
                       position, n: '1' if c[position] >= n - c[position] else '0')
co2_rating = rating(t.copy(), 0, lambda c,
                    position, n: '1' if c[position] < n - c[position] else '0')
print(int(oxygen_rating, 2) * int(co2_rating, 2))
