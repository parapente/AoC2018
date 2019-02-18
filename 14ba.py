#!/usr/bin/python3


with open('14.dat') as f:
    data = f.read()
# data = '59414'
recipies = list(data)
recipies = [int(x) for x in recipies]
print(recipies)
elf1 = 0
elf2 = 1
repbook = [3, 7]
len_input = len(recipies)
len_rep = len(repbook)
done = False
ldic = dict()
while not done:
    try:
        repbook += ldic[(repbook[elf1], repbook[elf2])]
    except KeyError:
        score = repbook[elf1] + repbook[elf2]
        if score >= 10:
            ldic[(repbook[elf1], repbook[elf2])] = list(divmod(score, 10))
            repbook += list(divmod(score, 10))
        else:
            ldic[(repbook[elf1], repbook[elf2])] = [score]
            repbook += [score]
    len_rep = len(repbook)
    elf1 = (elf1 + 1 + repbook[elf1]) % len_rep
    elf2 = (elf2 + 1 + repbook[elf2]) % len_rep
    done = (repbook[-len_input:] == recipies) | (repbook[-1-len_input:-1] == recipies)
    # print(len_rep, end='\r')
if repbook[-len_input:] == recipies:
    print(len_rep - len_input)
else:
    print(len_rep - len_input - 1)
