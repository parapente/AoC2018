#!/usr/bin/python3


def power_level(pos, serial):
    rackID = pos[0] + 10
    level = (((rackID * pos[1] + serial) * rackID) // 100) % 10 - 5
    return level


with open('11.dat') as f:
    data = f.read()
serial = int(data)
cells = [[0] * 300 for i in range(300)]
for i in range(300):
    for j in range(300):
        cells[i][j] = power_level([i, j], serial)
maxsum = 0
maxpos = []
for i in range(297):
    for j in range(297):
        sumcell = 0
        x = i
        endx = x + 3
        while x < endx:
            y = j
            endy = y + 3
            while y < endy:
                sumcell += cells[x][y]
                y += 1
            x += 1
        if maxsum < sumcell:
            maxsum = sumcell
            maxpos = [i, j]
print('Maximum at ', maxpos, 'with sum ', maxsum)
