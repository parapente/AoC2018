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
sd = dict()
while z <= 300:
    i = 0

    # while f > 0:
    #     if (z % f) == 0:
    #         divisor = f
    #         f = 0
    #     f -= 1
    # fraction = z // divisor
    # if z < 3 or (z % divisor) != 0:
    #     valid = False
    # else:
    #     valid = True
    while i < (300 - z):
        j = 0
        while j < (300 - z):
            sumcell = 0

            if z > 1:
                sumcell += sd[i, j, z-1]

                x = i
                endx = x + z
                y = j + (z - 1)
                while x < endx:
                    sumcell += cells[x][y]
                    x += 1

                y = j
                endy = y + z
                x = i + (z - 1)
                sumcell += sum(cells[x][y:endy])
                # while y < endy:
                #     sumcell += cells[x][y]
                #     y += 1
            else:
                sumcell = cells[i][j]

            sd[i, j, z] = sumcell
            # print('sd(', i, j, z, ')=', sumcell)
            if maxsum < sumcell:
                maxsum = sumcell
                maxpos = [i, j]
                maxz = z
            j += 1
        i += 1
    print('z: ', z, ' - maxsum:', maxsum, maxpos, maxz)
    z += 1
print('Maximum at ', maxpos, 'with sum ', maxsum, ' square size: ', maxz)
