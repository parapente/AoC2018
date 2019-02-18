#!/usr/bin/python3
import time
from queue import Queue


class Unit():

    def __init__(self, pos, unittype):
        self.pos = pos
        self.hp = 200
        self.attack = 3
        self.type = unittype

    def __repr__(self):
        return str(self.pos) + " HP:" + str(self.hp)

    def __str__(self):
        return str(self.pos) + " HP:" + str(self.hp)


def print_status():
    print(chr(27) + "[2J")
    print(chr(27) + "[H")
    for line in world:
        print(''.join(line))
    print('Elves:', elves)
    print('Goblins:', goblins)


def neighbors(pos, enemy):
    neigh = []
    if (pos[0] - 1 >= miny and world[pos[0] - 1, pos[1]] == '.') or pos == enemy.pos:
        neigh.append([pos[0] - 1, pos[1]])
    if (pos[1] - 1 >= minx and world[pos[0], pos[1] - 1] == '.') or pos == enemy.pos:
        neigh.append([pos[0], pos[1] - 1])
    if (pos[1] + 1 <= maxx and world[pos[0], pos[1] + 1] == '.') or pos == enemy.pos:
        neigh.append([pos[0], pos[1] + 1])
    if (pos[0] + 1 <= maxy and world[pos[0] + 1, pos[1]] == '.') or pos == enemy.pos:
        neigh.append([pos[0] + 1, pos[1]])
    return neigh


def move(unit):
    if unit.type == 'G':
        enemies = elves
    else:
        enemies = goblins
    distance = []
    for enemy in enemies:
        start = unit.pos
        frontier = Queue()
        frontier.put(start)
        came_from = {}
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()
            for next in neighbors(current, enemy):
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current

        current = enemy.pos
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.reverse()
        distance.append([enemy, path[:]])


def attack(unit):
    pass


units = []
elves = []
goblins = []
minx = 0
miny = 0
maxx = 0
maxy = 0
with open('15.dat') as f:
    data = f.read()
world = data.split('\n')
world.pop()
for i, val in enumerate(world):
    world[i] = list(world[i])
for y, line in enumerate(world):
    for x, val in enumerate(line):
        if val in ('G', 'E'):
            units.append(Unit([y, x], val))
maxx = len(world[0]) - 1
maxy = len(world) - 1
units.sort(key=lambda unit: unit.pos)
elves = [x for x in units if x.type == 'E']
goblins = [x for x in units if x.type == 'G']
print_status()
time.sleep(0.1)
while elves and goblins:
    for unit in units:
        move(unit)
        attack(unit)
    print_status()
    time.sleep(0.1)
