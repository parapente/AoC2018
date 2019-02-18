#!/usr/bin/python3
import re
import ast


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
ops = [addr, addi, mulr, muli, banr, bani, borr, bori,
       setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
with open('16.dat') as f:
    data = f.read()
lines = data.split('\n')
ln = 0
done = False
samples = 0
while not done:
    m = re.match('Before: ([\\[\\]\\d, ]+)', lines[ln])
    if m:
        regb = ast.literal_eval(m.group(1))
        regb = [int(x) for x in regb]
        ln += 1
        top = lines[ln].split(' ')
        top = [int(x) for x in top]
        ln += 1
        m = re.match('After:  ([\\[\\]\\d, ]+)', lines[ln])
        rega = ast.literal_eval(m.group(1))
        rega = [int(x) for x in rega]
        ln += 2
        match = 0
        match_list = []
        for op in ops:
            reg = regb[:]
            op(top[1], top[2], top[3])
            if reg == rega:
                match += 1
                match_list.append(str(op))
        if (match > 2):
            samples += 1
            print('Op: ', top, 'In: ', regb, 'Out: ', rega, '-', match, 'matches!', match_list)
    else:
        done = True
print(samples, ' samples behave like three or more opcodes')
