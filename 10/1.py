with open('in.txt', 'r') as f:
    t = [i for i in f.read().split()]

opening = ('(', '[', '{', '<')
closing = {')': '(', ']': '[', '}': '{', '>': '<'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in t:
    stack = []
    for k, i in enumerate(line):
        if i in opening:
            stack.append(i)
        elif stack[-1] != closing[i]:
            score += scores[i]
            break
        else:
            stack.pop()
print(score)
