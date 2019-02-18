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
maxz = 0
z = 1
while z <= 300:
    for i in range(300 - z):
        for j in range(300 - z):
            sumcell = 0
            x = i
            endx = x + z
            while x < endx:
                y = j
                endy = y + z
                while y < endy:
                    sumcell += cells[x][y]
                    y += 1
                x += 1
            if maxsum < sumcell:
                maxsum = sumcell
                maxpos = [i, j]
                maxz = z
    z += 1
    print('z: ', z)
print('Maximum at ', maxpos, 'with sum ', maxsum, ' square size: ', maxz)
