#!/usr/bin/python3


mapdata = [['#', '?', '#'], ['?', 'X', '?'], ['#', '?', '#']]
tmppos = [1, 1]
exitpos = []
posstack = []
shortestpath = 0
tmpgroup = []
groupstack = []
tmplen = 0
with open('20.dat') as f:
    data = f.read()
regstr = data.split('\n')
regstr.pop()
regstr = regstr[0]
print(regstr)
i = 1
while i < (len(regstr) - 1):
    # for line in mapdata:
    #     print('=', ''.join(line), '=', sep='')
    # print(regstr[i])
    if regstr[i] == '(':
        print(tmppos)
        posstack.append(tmppos[:])
        if not groupstack:
            shortestpath += tmplen
        else:
            tmpgroup.append(tmplen)
        tmplen = 0
        groupstack.append([])
        tmpgroup = groupstack[-1]
        print(shortestpath, groupstack, tmpgroup)
    if regstr[i] == ')':
        tmppos = exitpos
        posstack.pop()
        tmpgroup.append(tmplen)
        if 0 in tmpgroup:
            smax = 0
        else:
            smax = max(tmpgroup)
        groupstack.pop()
        if not groupstack:
            shortestpath += smax
            tmplen = 0
        else:
            tmpgroup = groupstack[-1]
            tmplen = tmpgroup.pop()
            tmplen += smax
        print(shortestpath, groupstack, tmpgroup)
    if regstr[i] == '|':
        exitpos = tmppos
        tmppos = posstack.pop()
        posstack.append(tmppos[:])
        print(tmppos)
        tmpgroup.append(tmplen)
        tmplen = 0
        print(shortestpath, groupstack, tmpgroup)
    if regstr[i] not in ('|', '(', ')'):
        tmplen += 1
    if regstr[i] == 'W':
        mapdata[tmppos[0]][tmppos[1] - 1] = '|'
        if (tmppos[1] - 2) < 0:
            # Add 2 new columns to the left
            print('Add')
            for z, val in enumerate(posstack):
                posstack[z][1] += 2
            for y, yval in enumerate(mapdata):
                if y in (tmppos[0] - 1, tmppos[0] + 1):
                    mapdata[y] = ['#', '?'] + mapdata[y]
                else:
                    if y == tmppos[0]:
                        mapdata[y] = ['?', '.'] + mapdata[y]
                    else:
                        mapdata[y] = [' ', ' '] + mapdata[y]
            # tmppos doesn't need to change
        else:
            y, x = tmppos
            mapdata[y - 1][x - 3] = '#'
            if mapdata[y - 1][x - 2] == ' ':
                mapdata[y - 1][x - 2] = '?'
            if mapdata[y][x - 2] == ' ':
                mapdata[y][x - 2] = '.'
            mapdata[y + 1][x - 3] = '#'
            if mapdata[y + 1][x - 2] == ' ':
                mapdata[y + 1][x - 2] = '?'
            tmppos[1] -= 2
    if regstr[i] == 'E':
        mapdata[tmppos[0]][tmppos[1] + 1] = '|'
        if (tmppos[1] + 2) > (len(mapdata[0]) - 1):
            # Add 2 new columns to the right
            print('Add')
            for y, yval in enumerate(mapdata):
                if y in (tmppos[0] - 1, tmppos[0] + 1):
                    mapdata[y] = mapdata[y] + ['?', '#']
                else:
                    if y == tmppos[0]:
                        mapdata[y] = mapdata[y] + ['.', '?']
                    else:
                        mapdata[y] = mapdata[y] + [' ', ' ']
            tmppos[1] += 2
        else:
            y, x = tmppos
            mapdata[y - 1][x + 3] = '#'
            if mapdata[y - 1][x + 2] == ' ':
                mapdata[y - 1][x + 2] = '?'
            if mapdata[y][x + 3] == ' ':
                mapdata[y][x + 3] = '?'
            if mapdata[y][x + 2] == ' ':
                mapdata[y][x + 2] = '.'
            mapdata[y + 1][x + 3] = '#'
            if mapdata[y + 1][x + 2] == ' ':
                mapdata[y + 1][x + 2] = '?'
            tmppos[1] += 2
    if regstr[i] == 'N':
        mapdata[tmppos[0] - 1][tmppos[1]] = '-'
        if (tmppos[0] - 2) < 0:
            # Add 2 new rows to the top
            print('Add')
            for z, val in enumerate(posstack):
                posstack[z][0] += 2
            row1 = []
            row2 = []
            for x, xval in enumerate(mapdata[0]):
                if x in (tmppos[1] - 1, tmppos[1] + 1):
                    row1 += '#'
                    row2 += '?'
                else:
                    if x == tmppos[1]:
                        row1 += '?'
                        row2 += '.'
                    else:
                        row1 += ' '
                        row2 += ' '
            mapdata = [row1, row2] + mapdata
            # tmppos doesn't need to change
        else:
            y, x = tmppos
            mapdata[y - 3][x - 1] = '#'
            if mapdata[y - 2][x - 1] == ' ':
                mapdata[y - 2][x - 1] = '?'
            if mapdata[y - 3][x] == ' ':
                mapdata[y - 3][x] = '?'
            if mapdata[y - 2][x] == ' ':
                mapdata[y - 2][x] = '.'
            mapdata[y - 3][x + 1] = '#'
            if mapdata[y - 2][x + 1] == ' ':
                mapdata[y - 2][x + 1] = '?'
            tmppos[0] -= 2
    if regstr[i] == 'S':
        mapdata[tmppos[0] + 1][tmppos[1]] = '-'
        if (tmppos[0] + 2) > (len(mapdata) - 1):
            # Add 2 new rows to the bottom
            print('Add')
            row1 = []
            row2 = []
            for x, xval in enumerate(mapdata[0]):
                if x in (tmppos[1] - 1, tmppos[1] + 1):
                    row1 += '?'
                    row2 += '#'
                else:
                    if x == tmppos[1]:
                        row1 += '.'
                        row2 += '?'
                    else:
                        row1 += ' '
                        row2 += ' '
            mapdata = mapdata + [row1, row2]
            tmppos[0] += 2
        else:
            y, x = tmppos
            mapdata[y + 3][x - 1] = '#'
            if mapdata[y + 2][x - 1] == ' ':
                mapdata[y + 2][x - 1] = '?'
            if mapdata[y + 3][x] == ' ':
                mapdata[y + 3][x] = '?'
            if mapdata[y + 2][x] == ' ':
                mapdata[y + 2][x] = '.'
            mapdata[y + 3][x + 1] = '#'
            if mapdata[y + 2][x + 1] == ' ':
                mapdata[y + 2][x + 1] = '?'
            tmppos[0] += 2
    i += 1

for y, yval in enumerate(mapdata):
    for x, xval in enumerate(yval):
        if xval == '?':
            mapdata[y][x] = '#'

for line in mapdata:
    print('=', ''.join(line), '=', sep='')
shortestpath += tmplen
print(shortestpath)
