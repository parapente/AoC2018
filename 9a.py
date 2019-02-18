#!/usr/bin/python3
import re


def start_game(num_players, turns):
    players = [0] * num_players
    table = [0]
    cur_marble = 0
    next_marble = 1
    turn = 1
    while turn <= turns:
        cur_player = (turn - 1) % num_players
        if next_marble % 23 == 0:
            pos = (cur_marble - 6) % len(table)
            players[cur_player] += table.pop(pos) + next_marble
            cur_marble = pos - 1
        else:
            pos = (cur_marble + 2) % len(table)
            table.insert(pos + 1, next_marble)
            cur_marble = pos
        next_marble += 1

        # Print table
        # print('[', cur_player + 1, ']', sep='', end='')
        # i = 0
        # for item in table:
        #     if i == cur_marble + 1:
        #         print(' (', item, ') ', sep='', end='')
        #     else:
        #         print(' ', item, ' ', sep='', end='')
        #     i += 1
        # print()

        turn += 1
    print('High score: ', max(players))


with open('9.dat') as f:
    data = f.read()
data = data.split('\n')
data.pop()
m = re.match('(\\d+).+ (\\d+) points', data[0])
gamedata = [m.group(1), m.group(2)]
print(gamedata)
print('[-] (0)')
start_game(int(gamedata[0]), int(gamedata[1]))
