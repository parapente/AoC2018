#!/usr/bin/python3


with open('14.dat') as f:
    data = f.read()
recipies = int(data)
print(recipies)
elf1 = 0
elf2 = 1
# repbook = [recipies[0], recipies[1]]
repbook = [3, 7]
while len(repbook) < recipies + 10:
    # for i, val in enumerate(repbook):
    #     if i == elf1:
    #         print('(', val, ')', sep='', end='')
    #     else:
    #         if i == elf2:
    #             print('[', val, ']', sep='', end='')
    #         else:
    #             print(' ', val, ' ', sep='', end='')
    # print()

    score = repbook[elf1] + repbook[elf2]
    if score >= 10:
        repbook.append(score // 10)
        repbook.append(score % 10)
    else:
        repbook.append(score)
    elf1 = (elf1 + 1 + repbook[elf1]) % len(repbook)
    elf2 = (elf2 + 1 + repbook[elf2]) % len(repbook)
# for i, val in enumerate(repbook):
#     if i == elf1:
#         print('(', val, ')', sep='', end='')
#     else:
#         if i == elf2:
#             print('[', val, ']', sep='', end='')
#         else:
#             print(' ', val, ' ', sep='', end='')
# print()
z = 0
for i, val in enumerate(repbook):
    if i > (recipies-1) and z < 10:
        print(val, sep='', end='')
        z += 1
print()
