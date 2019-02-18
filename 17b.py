#!/usr/bin/python3
import re


with open('17.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
clay = []
for line in lines:
    m = re.search('x=([\\d.]+)', line)
    x = m.group(1).split('..')
    m = re.search('y=([\\d.]+)', line)
    y = m.group(1).split('..')
    if len(x) == 2:
        y = int(y[0])
        i = int(x[0])
        while i <= int(x[1]):
            clay.append([i, y])
            i += 1
    else:
        if len(y) == 2:
            x = int(x[0])
            i = int(y[0])
            while i <= int(y[1]):
                clay.append([x, i])
                i += 1
clay.sort(key=lambda x: x[1])
miny = clay[0][1]
maxy = clay[-1][1]
clay.sort(key=lambda x: x[0])
minx = clay[0][0] - 1
maxx = clay[-1][0] + 1
# print(minx, miny, maxx, maxy)
ground = [['.'] * (maxx - minx) for i in range(maxy - miny + 2)]
ground[0][500 - minx] = '+'
for point in clay:
    ground[point[1] - miny + 1][point[0] - minx] = '#'
# for line in ground:
#     print(''.join(line))

flow = [[0, 500 - minx]]
# print(len(flow))
# print(maxy, miny)
while flow:
    point = flow[-1]
    if point[0] > (maxy - miny):
        flow.pop()
    else:
        if ground[point[0] + 1][point[1]] == '.':
            ground[point[0] + 1][point[1]] = '|'
            flow.append([point[0] + 1, point[1]])
        else:
            if ground[point[0] + 1][point[1]] in ['#', '~']:
                flow.pop()
                blocks = [[point[0], point[1]]]
                # We need to check if the water settles or not
                x = point[1]
                left_blocked = False
                right_blocked = False
                while x >= 0 and ground[point[0] + 1][x] in ['#', '~'] and ground[point[0]][x - 1] != '#':
                    x -= 1
                    blocks.append([point[0], x])
                if x >= 0:
                    if ground[point[0] + 1][x] == '.':
                        # Water pours out
                        flow.append([point[0], x])
                    else:
                        left_blocked = True
                else:
                    print('Negative X!!! Abort! Abort!')
                    exit(1)
                x = point[1]
                while x >= 0 and ground[point[0] + 1][x] in ['#', '~'] and ground[point[0]][x + 1] != '#':
                    x += 1
                    blocks.append([point[0], x])
                if x <= (maxx - minx):
                    if ground[point[0] + 1][x] == '.':
                        # Water pours out
                        flow.append([point[0], x])
                    else:
                        right_blocked = True
                else:
                    print('X above and beyond!!! Abort! Abort!')
                    exit(1)
                if left_blocked and right_blocked:
                    for block in blocks:
                        ground[block[0]][block[1]] = '~'
                else:
                    for block in blocks:
                        ground[block[0]][block[1]] = '|'
            else:
                if ground[point[0] + 1][point[1]] == '|':
                    flow.pop()
    # print(flow)

water = 0
for line in ground:
    for point in line:
        if point == '~':
            water += 1
    # print(''.join(line))
print(water)
