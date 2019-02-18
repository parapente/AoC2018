#!/usr/bin/python3


def find_pair():
    global prev
    for i, value in enumerate(polymer):
        if (value.isupper() and prev.islower() and prev.upper() == value) or (value.islower() and prev.isupper() and value.upper() == prev):
            return [i-1, i]
        prev = value
    return False


with open('5.dat') as f:
    data = f.read()
polymer = data.rstrip()
polymer = list(polymer)
prev = '-'
pair = find_pair()
print(len(polymer))
while pair:
    polymer.pop(pair[0])
    polymer.pop(pair[0])
    prev = '-'
    pair = find_pair()
    print(len(polymer))
print(''.join(polymer))
