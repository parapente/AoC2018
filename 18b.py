#!/usr/bin/python3
from time import time


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

state = dict()
statelist = []
cycle = 0
cycle_found = False
cycle_start = 0
start = ''
for line in area:
    start += ''.join(line)
    print(''.join(line))
print()
end = ''
perc = 0
prevtime = 0
for i in range(1000000000):
    try:
        if not cycle_found:
            end = state[start]
            statelist.append(start)
            if end == statelist[0]:
                # Found cycle
                cycle = len(statelist)
                cycle_found = True
                cycle_start = i
        else:
            break
        # print('Here!')
        # chunks, chunk_size = len(end), len(end)//len(area)
        # tmp = [end[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
        # for y, yval in enumerate(area):
        #     area[y] = list(tmp[y])
    except KeyError:
        end = ''
        for y, yval in enumerate(area):
            for x, xval in enumerate(yval):
                newarea[y][x] = calc(y, x)
        for y, yval in enumerate(area):
            area[y] = newarea[y][:]
            end += ''.join(newarea[y])
            # print(''.join(newarea[y]))
        # print()
        state[start] = end
    start = end
    newperc = i / 1000000000
    if newperc - perc > 0.01:
        newtime = time()
        endtime = (newtime - prevtime) * (10000 - newperc)
        prevtime = newtime
        print('{:.2f}'.format(newperc), '% Ending in {:.0f}'.format(endtime), 'secs', sep='', end='\r')
        perc = newperc

end = statelist[(1000000000 - 1 - cycle_start) % cycle]
chunks, chunk_size = len(end), len(end)//len(area)
tmp = [end[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
for y, yval in enumerate(area):
    area[y] = list(tmp[y])

stat = {'.': 0, '|': 0, '#': 0}

for y, yval in enumerate(area):
    for x, xval in enumerate(yval):
        stat[xval] += 1
print(stat['|'] * stat['#'])
