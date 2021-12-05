def mark_board(board: list, value: int):
    return [[-1 if i == value else i for i in row] for row in board]


def check_board(board: list) -> bool:
    return any(all(i < 0 for i in row) for row in board) or any(
        all(i < 0 for i in column) for column in zip(*board))


def calculate_score(value: int, board: list) -> int:
    return sum(i if i >= 0 else 0 for row in board for i in row) * value


def check_boards(boards: list, values: list):
    for value in values:
        for index in range(len(boards)):
            boards[index] = mark_board(boards[index], value)
            if check_board(boards[index]):
                return calculate_score(value, boards[index])


with open('in.txt', mode='r') as f:
    values = [int(i) for i in f.readline().split(",")]
    next(f)
    boards = [[[int(i) for i in row.split()] for row in board.splitlines()]
              for board in f.read().split('\n\n')]
score = check_boards(boards, values)
print(score)