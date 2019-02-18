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
data = data.rstrip()
polymer = list(data)
orig = data
letters = set(list(orig.upper()))
min_unit = ['', 99999]
for letter in letters:
    print('Removing ', letter, '/', letter.lower())
    polymer = orig.replace(letter, '')
    polymer = list(polymer.replace(letter.lower(), ''))
    prev = '-'
    pair = find_pair()
    while pair:
        polymer.pop(pair[0])
        polymer.pop(pair[0])
        prev = '-'
        pair = find_pair()
    print('Min len: ', len(polymer))
    if len(polymer) < min_unit[1]:
        min_unit = [letter, len(polymer)]
print('Result: ', min_unit)
