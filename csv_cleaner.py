# -*- coding: utf-8 -*-
import sys

with open(sys.argv[1], 'r', encoding='UTF8') as in_file, open(sys.argv[1][:-3] + 'clean.csv', 'w', encoding='UTF8') as out_file:
    seen = set()
    for line in in_file:
        line = line.strip()
        if line not in seen:
            seen.add(line)
            print(line, file=out_file)
