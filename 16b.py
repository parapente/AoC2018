#!/usr/bin/python3


def addr(a, b, c):
    global reg
    reg[c] = reg[a] + reg[b]


def addi(a, b, c):
    global reg
    reg[c] = reg[a] + b


def mulr(a, b, c):
    global reg
    reg[c] = reg[a] * reg[b]


def muli(a, b, c):
    global reg
    reg[c] = reg[a] * b


def banr(a, b, c):
    global reg
    reg[c] = reg[a] & reg[b]


def bani(a, b, c):
    global reg
    reg[c] = reg[a] & b


def borr(a, b, c):
    global reg
    reg[c] = reg[a] | reg[b]


def bori(a, b, c):
    global reg
    reg[c] = reg[a] | b


def setr(a, b, c):
    global reg
    reg[c] = reg[a]


def seti(a, b, c):
    global reg
    reg[c] = a


def gtir(a, b, c):
    global reg
    if a > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0


def gtri(a, b, c):
    global reg
    if reg[a] > b:
        reg[c] = 1
    else:
        reg[c] = 0


def gtrr(a, b, c):
    global reg
    if reg[a] > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0


def eqir(a, b, c):
    global reg
    if a == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0


def eqri(a, b, c):
    global reg
    if reg[a] == b:
        reg[c] = 1
    else:
        reg[c] = 0


def eqrr(a, b, c):
    global reg
    if reg[a] == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0


reg = [0, 0, 0, 0]
ops = [borr, addr, eqrr, addi, eqri, eqir, gtri, mulr,
       setr, gtir, muli, banr, seti, gtrr, bani, bori]
with open('16.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
start = False
empty = 0
for line in lines:
    if start:
        op = line.split(' ')
        op = [int(x) for x in op]
        ops[op[0]](op[1], op[2], op[3])
    else:
        if line == '':
            empty += 1
        else:
            empty = 0
        if empty == 3:
            start = True
print('Register 0:', reg[0])
