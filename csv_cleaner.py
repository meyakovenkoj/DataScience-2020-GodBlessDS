import sys

with open(sys.argv[1], 'r') as in_file, open(sys.argv[1][:-3] + 'clean.csv', 'w') as out_file:
    seen = set()
    for line in in_file:
        if line not in seen:
            seen.add(line)
            out_file.write(line)
