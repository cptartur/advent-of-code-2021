from functools import reduce

with open('in.txt', 'r') as f:
    t = [i for i in f.read().split()]

opening = ('(', '[', '{', '<')
closing = {')': '(', ']': '[', '}': '{', '>': '<'}
brackets_values = {'(': 1, '[': 2, '{': 3, '<': 4}

scores = []
for line in t:
    stack = []
    for i in line:
        if i in opening:
            stack.append(i)
        elif stack[-1] != closing[i]:
            break
        else:
            stack.pop()
    else:
        if len(stack) != 0:
            local_score = reduce(
                lambda x, y: x * 5 + y,
                reversed(list(map(brackets_values.get, stack)) + [0]))
            scores.append(local_score)
print(sorted(scores)[len(scores) // 2])
