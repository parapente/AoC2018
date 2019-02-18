#!/usr/bin/python3
import re


def mandist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + \
           abs(point1[2] - point2[2])


with open('23.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
nanobot = []
nanorange = []
maxrange = 0
maxi = 0
i = 0
for line in lines:
    m = re.match('pos=<(-*\\d+),(-*\\d+),(-*\\d+)>, r=(-*\\d+)', line)
    nanobot.append([int(m.group(1)), int(m.group(2)), int(m.group(3))])
    nanorange.append(int(m.group(4)))
    if nanorange[-1] > maxrange:
        maxrange = nanorange[-1]
        maxi = i
    i += 1
print(maxi, maxrange)
point = nanobot[maxi][:]
print(point)
inrange = 0
for n in nanobot:
    if mandist(point, n) <= maxrange:
        inrange += 1
print(inrange)
