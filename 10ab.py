#!/usr/bin/python3
import re


with open('10.dat') as f:
    data = f.read()
data = data.split('\n')
data.pop()
positions = []
velocities = []
expr = re.compile('([-]*\\d+)')
for line in data:
    m = expr.findall(line)
    positions.append([int(m[0]), int(m[1])])
    velocities.append([int(m[2]), int(m[3])])

bkp_pos = positions[:]
area = 9999999999999
newarea = 999999999999
sec = 0
while newarea < area:
    area = newarea
    minx = miny = 99999
    maxx = maxy = -99999
    for pos in positions:
        if minx > pos[0]:
            minx = pos[0]
        if miny > pos[1]:
            miny = pos[1]
        if maxx < pos[0]:
            maxx = pos[0]
        if maxy < pos[1]:
            maxy = pos[1]
    newarea = (maxx - minx) * (maxy - miny)
    # print('[', sec, ']', minx, miny, maxx, maxy, ' - newarea: ', newarea)
    for i, val in enumerate(positions):
        positions[i][0] += velocities[i][0]
        positions[i][1] += velocities[i][1]
    sec += 1

for z in range(2):
    sec -= 1
    for i, val in enumerate(positions):
        positions[i][0] -= velocities[i][0]
        positions[i][1] -= velocities[i][1]
minx = miny = 99999
maxx = maxy = -99999
for pos in positions:
    if minx > pos[0]:
        minx = pos[0]
    if miny > pos[1]:
        miny = pos[1]
    if maxx < pos[0]:
        maxx = pos[0]
    if maxy < pos[1]:
        maxy = pos[1]
newarea = (maxx - minx) * (maxy - miny)
print('[', sec, ']', minx, miny, maxx, maxy, ' - newarea: ', newarea)
sky = [['.'] * (maxy - miny + 1) for i in range(maxx - minx + 1)]
for pos in positions:
    # print(pos[0], pos[1])
    # print(pos[0] - minx, pos[1] - miny)
    sky[pos[0] - minx][pos[1] - miny] = '#'

for y in range(maxy - miny + 1):
    for x in range(maxx - minx + 1):
        print(sky[x][y], sep='', end='')
    print()
