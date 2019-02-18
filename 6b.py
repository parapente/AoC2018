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
for i in range(len(points)):
    points[i] = [int(points[i][1]), int(points[i][0])]
space = [['.'] * 1000 for i in range(1000)]
limit = 10000
areasize = 0
for y in range(1000):
    for x in range(1000):
        totaldis = 0
        for point in points:
            totaldis += manhattan([y, x], point)
        if totaldis < limit:
            space[y][x] = '#'
            areasize += 1

print(areasize)
