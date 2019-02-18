#!/usr/bin/python3
import re


with open('12.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()

# Read initial state
m = re.search('([.#]+)', lines[0])
init_state = m.group(1)

# Read rules
rules = dict()
i = 2
while i < len(lines):
    rule = lines[i].split(' => ')
    rules[rule[0]] = rule[1]
    i += 1

pots = ['.'] * 3 + list(init_state)
base = 3

generation = 0
print(generation, ': ', ''.join(pots[base-3:]), sep='')
perc = 0
while generation < 500:
    generation += 1

    m = re.match('([.]+)', ''.join(pots[0:5]))
    if m is None:
        pots = (['.'] * 5) + pots
        base += 5
    else:
        if len(m.group(1)) < 5:
            pots = (['.'] * (5 - len(m.group(1)))) + pots
            base += 5 - len(m.group(1))

    m = re.search('([.]+)$', ''.join(pots[-5:]))
    if m is None:
        pots += (['.'] * 5)
    else:
        if len(m.group(1)) < 5:
            pots = pots + (['.'] * (5 - len(m.group(1))))

    newpots = pots[:]
    for z in range(len(pots) - 5):
        newpots[z + 2] = rules[''.join(pots[z:z + 5])]
    pots = newpots
    print(generation, ': ', ''.join(pots[base-3:]), sep='')
    # newperc = (generation / 50000000000) * 100
    # if newperc - perc > 0.01:
    #     print('{:.2f}'.format(newperc), '%', end='\r')
    #     perc = newperc

    sumpots = 0
    val = -base
    for pot in pots:
        if pot == '#':
            sumpots += val
        val += 1
    print('Sum:', sumpots)
