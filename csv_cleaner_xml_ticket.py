# -*- coding: utf-8 -*-
import sys

with open(sys.argv[1], 'r', encoding='UTF8') as in_file, open(sys.argv[1][:-3] + 'clean.csv', 'w', encoding='UTF8') as out_file:
    seen = dict()
    for line in in_file:
        line = line.strip()
        linesplit = line.split(',')
        key = linesplit[0]+','+linesplit[1]
        print(key)
        if key not in seen:
            seen[key] = linesplit[2]
        else:
	        if (seen[key] != ''):
	        	seen[key] = linesplit[2]
    for key in seen:
        print(key+','+seen[key], file=out_file)
