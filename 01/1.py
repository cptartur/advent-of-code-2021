with open("in.txt", "r") as f:
    t = list(map(int, f.read().splitlines()))

increases = [1 for i in range(1, len(t)) if t[i] > t[i - 1]]
print(increases.count(1))
