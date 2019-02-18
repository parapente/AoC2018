#!/usr/bin/python3


with open('2.dat') as f:
    data = f.read()
box = data.split("\n")
box.pop()
two = 0
three = 0
for b in box:
    letters = dict()
    for c in b:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    ttwo = 0
    tthree = 0
    for key in letters:
        if letters[key] == 2:
            ttwo += 1
        if letters[key] == 3:
            tthree += 1
    if ttwo:
        two += 1
    if tthree:
        three += 1
checksum = two * three
print("Checksum:", checksum)
