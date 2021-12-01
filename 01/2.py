with open("in.txt", "r") as f:
    t = list(map(int, f.read().splitlines()))

sums = [sum(t[i:min(i + 3, len(t))]) for i in range(len(t))]
increases = [1 for i in range(1, len(sums)) if sums[i] > sums[i - 1]]
print(increases.count(1))
