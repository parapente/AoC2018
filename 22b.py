#!/usr/bin/python3


with open('22a.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
depth = int(lines[0].split(' ')[1])
target = lines[1].split(' ')[1].split(',')
target = [int(x) for x in target]
print(depth, target)
cavemap = [['.']*(target[0] + 1) for x in range(target[1] + 1)]
erosion = [[0]*(target[0] + 1) for x in range(target[1] + 1)]
risk_lvl = 0
for y, yval in enumerate(cavemap):
    for x, xval in enumerate(yval):
        geol_idx = 0
        if (x == 0 and y == 0) or (x == target[0] and y == target[1]):
            geol_idx = 0
        else:
            if y == 0:
                geol_idx = x * 16807
            else:
                if x == 0:
                    geol_idx = y * 48271
                else:
                    geol_idx = erosion[y][x-1] * erosion[y-1][x]
        erosion[y][x] = (geol_idx + depth) % 20183
        reg_type = erosion[y][x] % 3
        if reg_type == 0:
            cavemap[y][x] = '.'
        else:
            if reg_type == 1:
                cavemap[y][x] = '='
                risk_lvl += 1
            else:
                cavemap[y][x] = '|'
                risk_lvl += 2

for line in cavemap:
    print(''.join(line))
