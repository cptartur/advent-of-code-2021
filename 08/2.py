with open('in.txt', 'r') as f:
    t = [i.split(' | ') for i in f.read().splitlines()]

base_lenghts = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

common = {
    (2, 3, 3, 6): 0,
    (1, 2, 2, 5): 2,
    (2, 3, 3, 5): 3,
    (1, 3, 2, 5): 5,
    (1, 3, 2, 6): 6,
    (2, 4, 3, 6): 9,
}

total = 0
for inputs, outputs in t:
    decoded_digits = {base_lenghts[len(i)]: frozenset(i)
                      for i in inputs.split(' ') if len(set(i)) in (2, 4, 3, 7)}

    def get_key(s): return common[tuple(len(set(s).intersection(
        decoded_digits[v])) for v in (1, 4, 7, 8))]
    decoded_digits.update({get_key(i): frozenset(i)
                          for i in inputs.split(' ') if len(i) not in base_lenghts})
    decoded_digits = {v: k for k, v in decoded_digits.items()}
    total += int(''.join(str(decoded_digits[frozenset(i)])
                 for i in outputs.split(' ')))
print(total)

"""
    1 4 7 8
0   2 3 3 6
2   1 2 2 5
3   2 3 3 5
5   1 3 2 5
6   1 3 1 6
9   2 4 3 6


"""
