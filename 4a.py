#!/usr/bin/python3
import re


with open('4.dat') as f:
    data = f.read()
log = data.split("\n")
log.pop()
log.sort()
# print(log)
duration = dict()
last_guard = ''
start = 0
end = 0
timetable = dict()
for line in log:
    m = re.match('\\[(\\d+)-(\\d+)-(\\d+) (\\d\\d):(\\d\\d)\\] (\\w+) ([#\\w]+)', ''.join(line))
    if m:
        year = m.group(1)
        month = m.group(2)
        day = m.group(3)
        hour = int(m.group(4))
        minute = int(m.group(5))
        w1 = m.group(6)
        w2 = m.group(7)

        if w1 == 'Guard':
            last_guard = w2
        else:
            if w1 == 'falls':
                start = minute
            if w1 == 'wakes':
                end = minute
                if last_guard in duration:
                    duration[last_guard] += end - start
                else:
                    duration[last_guard] = end - start
                key = str(month)+'-'+str(day)
                if key not in timetable:
                    timetable[key] = [last_guard, ['.']*start+['#']*(end-start)+['.']*(60-end)]
                else:
                    timetable[key][1] = timetable[key][1][:start]+['#']*(end-start)+timetable[key][1][end:]
    else:
        print("Failed match on ", line)
        exit()
max_dur = 0
max_dur_id = ''
for key in duration:
    if duration[key] > max_dur:
        max_dur = duration[key]
        max_dur_id = key
table = []
mins = dict()
for key in timetable:
    table.append(key + ' ' + timetable[key][0] + ' \t' + ''.join(timetable[key][1]))
    if timetable[key][0] == max_dur_id:
        i = 0
        for item in timetable[key][1]:
            if item == '#':
                if i in mins:
                    mins[i] += 1
                else:
                    mins[i] = 1
            i += 1

table.sort()
for line in table:
    print(line)
# print(duration)
print('Guard with id ', max_dur_id, ' spend the most minutes asleep (', max_dur, ')')
max_min = 0
max_min_id = -1
for key in mins:
    if mins[key] > max_min:
        max_min = mins[key]
        max_min_id = key
print('The guard was asleep most during minute', max_min_id)
print(int(max_dur_id.split('#')[1])*int(max_min_id))
