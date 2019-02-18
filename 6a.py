#!/usr/bin/python3


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


with open('6.dat') as f:
    data = f.read()
points = data.split('\n')
points.pop()
for i in range(len(points)):
    points[i] = points[i].split(', ')
minx = 999
miny = 999
maxx = 0
maxy = 0
for i in range(len(points)):
    points[i] = [int(points[i][1]), int(points[i][0])]
    if points[i][0] < miny:
        miny = points[i][0]
    if points[i][1] < minx:
        minx = points[i][1]
    if points[i][0] > maxy:
        maxy = points[i][0]
    if points[i][1] > maxx:
        maxx = points[i][1]
print(minx, miny, maxx, maxy)
space = [['.'] * (maxx - minx + 2) for i in range(maxy - miny + 2)]
counted = 0
y = miny - 1
while y < maxy + 1:
    x = minx - 1
    while x < maxx + 1:
        if [y, x] in points:
            space[y - miny + 1][x - minx + 1] = 'X'
        mindis = [999, 999]
        dist = dict()
        for i, val in enumerate(points):
            dist[i] = manhattan([y, x], val)
        multiple = 0
        for key in dist:
            if dist[key] == mindis[0]:
                multiple += 1
            if dist[key] < mindis[0]:
                mindis = [dist[key], key]
                multiple = 1
        # print(y - miny + 1, x - minx + 1)
        if multiple > 1:
            space[y - miny + 1][x - minx + 1] = '.'
        else:
            space[y - miny + 1][x - minx + 1] = mindis[1]
        counted += 1
        perc = counted / ((maxy - miny + 2) * (maxx - minx + 2)) * 100
        print('{:.2f}%'.format(perc), end='\r')
        x += 1
    y += 1

# for line in space:
#     print(''.join(str(line)))
# Find infinite areas
y = miny - 1
x = minx - 1
while x < maxx + 1:
    if space[y - miny + 1][x - minx + 1] != '#':
        val = space[y - miny + 1][x - minx + 1]
        for j in range(maxy - miny + 2):
            for i in range(maxx - minx + 2):
                space[j][i] = space[j][i] if space[j][i] != val else '#'
    x += 1
y = miny - 1
x = minx - 1
while y < maxy + 1:
    if space[y - miny + 1][x - minx + 1] != '#':
        val = space[y - miny + 1][x - minx + 1]
        for j in range(maxy - miny + 2):
            for i in range(maxx - minx + 2):
                space[j][i] = space[j][i] if space[j][i] != val else '#'
    y += 1
y = maxy
x = minx - 1
while x < maxx + 1:
    if space[y - miny + 1][x - minx + 1] != '#':
        val = space[y - miny + 1][x - minx + 1]
        for j in range(maxy - miny + 2):
            for i in range(maxx - minx + 2):
                space[j][i] = space[j][i] if space[j][i] != val else '#'
    x += 1
y = miny - 1
x = maxx
while y < maxy + 1:
    if space[y - miny + 1][x - minx + 1] != '#':
        val = space[y - miny + 1][x - minx + 1]
        for j in range(maxy - miny + 2):
            for i in range(maxx - minx + 2):
                space[j][i] = space[j][i] if space[j][i] != val else '#'
    y += 1

# for line in space:
#     print(''.join(str(line)))
# Find sizes of different areas
areas = dict()
for line in space:
    for item in line:
        if is_digit(item):
            if item not in areas:
                areas[item] = 1
            else:
                areas[item] += 1

# Find largest area
largest = 0
print(areas)
for key in areas:
    if areas[key] > largest:
        largest = areas[key]
print('Largest area is ', largest)
