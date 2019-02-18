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


# The program with reg0=1 calculates the divisors of 10551329
# Unfortunately it takes ages...
reg = [1, 0, 0, 0, 0, 0]
ops = [borr, addr, eqrr, addi, eqri, eqir, gtri, mulr,
       setr, gtir, muli, banr, seti, gtrr, bani, bori]
with open('19.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
ip_reg = int(lines[0].split(' ')[1])
lines.pop(0)
ip = reg[ip_reg]
empty = 0
while 0 <= ip < len(lines):
    op = lines[ip].split(' ')
    op = [op[0]] + [int(x) for x in op[1:]]
    # print('.', end='')
    print(reg)
    globals()[op[0]](op[1], op[2], op[3])
    reg[ip_reg] += 1
    ip = reg[ip_reg]
print()
print('Register 0:', reg[0])
