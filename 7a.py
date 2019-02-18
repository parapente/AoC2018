#!/usr/bin/python3
import re


class Node:

    def __init__(self):
        self.prev = []
        self.next = []


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
while pieces:
    tmp = list(pieces)
    tmp.sort()
    last = ''
    for item in tmp:
        completed = True
        # print('Let\'s check item', item)
        # print('s[item].prev = ', s[item].prev)
        for i in s[item].prev:
            if i not in used:
                completed = False
        if completed:
            last = item
            break
    # print('Last: ', last)
    # print('s[last].next: ', s[last].next)
    pieces.remove(last)
    used.append(last)
    for item in s[last].next:
        if item not in used:
            pieces.add(item)
    # print('Pieces: ', pieces)
    # print('Used: ', used)
    # input()

print(''.join(used))
