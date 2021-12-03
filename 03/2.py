from collections import Counter


def remove_numbers(t: list, position: int) -> list:
    if (len(t)) == 1:
        return t
    t1 = t.copy()
    t1 = [list(map(lambda kv: kv[0] if kv[1] == '1' else None, enumerate(entry))) for entry in t]
    c = Counter(x for i in t for x in set(i) if x is not None)
    most_common = '1' if c[position] > len(t) - c[position] else '0'
    t = list(filter(lambda entry: entry[position] == most_common, t))
    remove_numbers(t, position + 1)
    

c = Counter()
with open('inx.txt', 'r') as f:
    t = [i for i in list(map(list, f.read().splitlines()))]
    # t = [list(map(lambda kv: kv[0] if kv[1] == '1' else None, enumerate(entry))) for entry in t]
    # c = Counter(x for i in t for x in set(i) if x is not None)

t1 = t.copy()
t1 = remove_numbers(t.copy(), 0)
print(t1)
# gamma_rate = "".join('1' if v > len(t) - v else '0' for _, v in sorted(c.items()))
# epsilon_rate = "".join('0' if v > len(t) - v else '1' for _, v in sorted(c.items()))
# print(int(gamma_rate, 2) * int(epsilon_rate, 2))