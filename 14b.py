#!/usr/bin/python3


with open('14.dat') as f:
    data = f.read()
recipies = data
print(recipies)
elf1 = 0
elf2 = 1
repbook = [3, 7]
check = '37'
done = False
while not done:
    score = repbook[elf1] + repbook[elf2]
    check = check + str(score)
    if score >= 10:
        repbook.append(score // 10)
        repbook.append(score % 10)
    else:
        repbook.append(score)
    len_rep = len(repbook)
    elf1 = (elf1 + 1 + repbook[elf1]) % len_rep
    elf2 = (elf2 + 1 + repbook[elf2]) % len_rep
    pos = check.find(recipies)
    if pos != -1:
        print(pos)
        done = True
    # print(len_rep, end='\r')
