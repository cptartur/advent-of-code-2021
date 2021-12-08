with open('in.txt', 'r') as f:
    t = [i.split(' | ') for i in f.read().splitlines()]

digits = [
    {'c', 'f'},
    {'b', 'c', 'd', 'f'},
    {'a', 'c', 'f'},
    {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
]

count = 0
for _, i in t:
    for segment in i.split(' '):
        if len(segment) in (2, 4, 3, 7):
            count += 1
print(count)
