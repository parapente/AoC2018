#!/usr/bin/python3
import re


class Piece():

    def __init__(self):
        self.id = 0
        self.offx = 0
        self.offy = 0
        self.width = 0
        self.height = 0


def cutpiece(p):
    global fabric
    for x in range(p.width):
        for y in range(p.height):
            if fabric[p.offx+x][p.offy+y] == '.':
                fabric[p.offx+x][p.offy+y] = p.id
            else:
                fabric[p.offx+x][p.offy+y] = 'X'


def checkpiece(p):
    intact = True
    for x in range(p.width):
        for y in range(p.height):
            if fabric[p.offx+x][p.offy+y] == 'X':
                intact = False
    return intact


def print_fabric():
    for f in fabric:
        print(''.join(f))


fabric = [['.']*1000 for i in range(1000)]
with open('3.dat') as f:
    data = f.read()
claims = data.split("\n")
claims.pop()
p = Piece()
for claim in claims:
    m = re.match('#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)', ''.join(claim))
    if m:
        p.id = m.group(1)
        p.offx = int(m.group(2))
        p.offy = int(m.group(3))
        p.width = int(m.group(4))
        p.height = int(m.group(5))
        cutpiece(p)
    else:
        print("Failed match on ", claim)
        exit()
for claim in claims:
    m = re.match('#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)', ''.join(claim))
    if m:
        p.id = m.group(1)
        p.offx = int(m.group(2))
        p.offy = int(m.group(3))
        p.width = int(m.group(4))
        p.height = int(m.group(5))
        if checkpiece(p):
            print('Piece: ', p.id, 'is intact!')
    else:
        print("Failed match on ", claim)
        exit()
