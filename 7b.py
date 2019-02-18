#!/usr/bin/python3
import re


class Node:

    def __init__(self):
        self.prev = []
        self.next = []


class Worker:

    def __init__(self):
        self.idle = True
        self.piece = '.'
        self.eta = 0


with open('7.dat') as f:
    data = f.read()
steps = data.split('\n')
steps.pop()
s = dict()
# Create next pointers
for step in steps:
    m = re.match('Step (\\w) .+ step (\\w)', step)
    if m.group(1) in s:
        s[m.group(1)].next.append(m.group(2))
    else:
        s[m.group(1)] = Node()
        s[m.group(1)].next.append(m.group(2))
    if m.group(2) not in s:
        s[m.group(2)] = Node()

# Create prev pointers
for step in steps:
    m = re.match('Step (\\w) .+ step (\\w)', step)
    s[m.group(2)].prev.append(m.group(1))

# Find starting point (prev = [])
pieces = set()
for key in s:
    # print('s[', key, ']=', s[key].next)
    if not s[key].prev:
        pieces.add(key)
        # print('Found key! ', key)
print('We start from', pieces)
used = []
workers = []
for i in range(5):
    workers.append(Worker())
workingon = []
second = 0

print('                         Workers')
print('Second   1       2       3       4       5       Done')
while pieces:
    for w in workers:
        if not w.idle:
            w.eta -= 1
            if w.eta == 0:
                pieces.remove(w.piece)
                workingon.remove(w.piece)
                used.append(w.piece)
                for item in s[w.piece].next:
                    if item not in used:
                        pieces.add(item)
                w.idle = True
                w.piece = '.'

    tmp = list(pieces)
    tmp.sort()

    for item in tmp:
        available = True
        if item in workingon:
            available = False
        else:
            for i in s[item].prev:
                if i not in used:
                    available = False
        if available:
            for w in workers:
                if w.idle:
                    w.piece = item
                    w.eta = 60 + ord(item) - ord('A') + 1
                    w.idle = False
                    workingon.append(item)
                    break

    print('{:4d}\t'.format(second), workers[0].piece,
          '\t', workers[1].piece, '\t', workers[2].piece,
          '\t', workers[3].piece, '\t', workers[4].piece,
          '\t', ''.join(used))
    second += 1

print(''.join(used))
