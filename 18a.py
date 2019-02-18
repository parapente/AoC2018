#!/usr/bin/python3


def calc(y, x):

    adj = {'.': 0, '#': 0, '|': 0}

    if y > 0:
        if x > 0:
            adj[area[y - 1][x - 1]] += 1
        adj[area[y - 1][x]] += 1
        if x < (len(area[0]) - 1):
            adj[area[y - 1][x + 1]] += 1

    if x > 0:
        adj[area[y][x - 1]] += 1
    if x < (len(area[0]) - 1):
        adj[area[y][x + 1]] += 1

    if y < (len(area) - 1):
        if x > 0:
            adj[area[y + 1][x - 1]] += 1
        adj[area[y + 1][x]] += 1
        if x < (len(area[0]) - 1):
            adj[area[y + 1][x + 1]] += 1
    if area[y][x] == '.' and adj['|'] > 2:
        return '|'
    if area[y][x] == '|' and adj['#'] > 2:
        return '#'
    if area[y][x] == '#':
        if adj['#'] > 0 and adj['|'] > 0:
            return '#'
        else:
            return '.'
    return str(area[y][x])


with open('18.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
area = [list(line) for line in lines]
newarea = [['.'] * len(area[0]) for i in enumerate(area)]

for line in area:
    print(''.join(line))
print()
for i in range(10):
    for y, yval in enumerate(area):
        for x, xval in enumerate(yval):
            newarea[y][x] = calc(y, x)
    for y, yval in enumerate(area):
        area[y] = newarea[y][:]
        print(''.join(newarea[y]))
    print()

stat = {'.': 0, '|': 0, '#': 0}

for y, yval in enumerate(area):
    for x, xval in enumerate(yval):
        stat[xval] += 1
print(stat['|'] * stat['#'])
