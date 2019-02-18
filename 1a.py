#!/usr/bin/python3


with open('1.dat') as f:
    key = f.read()
changes = key.split("\n")
changes.pop()
freq = 0
for c in changes:
    print("freq: ", freq, "change: ", c)
    freq += int(c)
print("Final freq: ", freq)
