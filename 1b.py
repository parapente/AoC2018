#!/usr/bin/python3


with open('1.dat') as f:
    key = f.read()
changes = key.split("\n")
changes.pop()
freq = 0
freqs = [0]
found = False
i = 0
while not found:
    c = changes[i]
    print("freq: ", freq, "change: ", c)
    freq += int(c)
    if freq in freqs:
        found = True
        print(freq, "frequency reached twice!")
    else:
        freqs.append(freq)
    i += 1
    i %= len(changes)
