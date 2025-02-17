# -*- coding: utf-8 -*-
import sys
import copy

with open(sys.argv[1], 'r', encoding='UTF8') as in_file, open(sys.argv[1][:-3] + 'clean.csv', 'w', encoding='UTF8') as out_file:
    seen = set()
    bad = set()
    for line in in_file:
        if line.strip():
            if ';;' not in line:
                seen.add(line)
                out_file.write(line)
                lst = line.split()
                line = lst[0]
                lst = lst[1:3] + ['',] + lst[4:] # data without b-day
                for i in lst:
                    line = line + ';' + i
                seen.add(line)
            else:
                bad.add(line)
        else:
            out_file.write(line)
    for line in bad:
        line2 = copy.copy(line)
        lst = line.split()
        line = lst[0]
        lst = lst[1:3] + ['',] + lst[4:] # data without b-day
        for i in lst:
            line = line + ';' + i
        if line not in seen: # if data not in seen but in bad - there was no data with b-day for such person
            out_file.write(line2)

out_file.close()
