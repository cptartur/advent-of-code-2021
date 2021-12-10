from functools import reduce
import operator


def check_neighbors(x: int, y: int, map: list[list]) -> bool:
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


def create_basin(x: int, y: int, map: list[list]):
    if (
        x not in range(len(map))
        or y not in range(len(map[0]))
        or map[x][y] == 9
        or map[x][y] == None
    ):
        return 0
    map[x][y] = None
    return (
        1
        + create_basin(x, y - 1, map)
        + create_basin(x + 1, y, map)
        + create_basin(x, y + 1, map)
        + create_basin(x - 1, y, map)
    )


with open('in.txt', 'r') as f:
    t = [list(map(int, i)) for i in f.read().splitlines()]

low_points = reduce(
    operator.add,
    map(
        lambda row: list(
            filter(
                lambda point: check_neighbors(*point, t),
                ((row[0], i) for i in range(len(row[1]))),
            )
        ),
        enumerate(t),
    ),
)
b = reduce(
    operator.mul,
    sorted(map(lambda point: create_basin(*point, t), low_points), reverse=True)[:3],
)
print(b)
