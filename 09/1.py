def check_neighbors(x: int, y: int, map: list):
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    value = map[x][y]
    for dx, dy in directions:
        if (
            x + dx in range(len(map))
            and y + dy in range(len(map[0]))
            and map[x + dx][y + dy] <= value
        ):
            return False
    return True


with open('in.txt', 'r') as f:
    t = [list(map(int, i)) for i in f.read().splitlines()]

total = 0
for x, row in enumerate(t):
    for y, point in enumerate(row):
        if check_neighbors(x, y, t):
            total += point + 1
print(total)
