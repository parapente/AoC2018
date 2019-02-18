#!/usr/bin/python3
import re

with open('2.dat') as f:
    data = f.read()
box = data.split("\n")
box.pop()
for b in box:
    tmp = list(b)
    for i, ival in enumerate(tmp):
        tmpstr = []
        for j, jval in enumerate(tmp):
            if j == i:
                tmpstr += "."
            else:
                tmpstr += jval
        tmpstr = ''.join(tmpstr)
        r = re.compile(tmpstr)
        found = list(filter(r.match, box))
        if found and len(found) == 2:
            print("match found: ", found)
            exit()
