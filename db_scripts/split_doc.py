with open('out.csv', 'w') as fout:
    with open('GodBlessDS_dbo_tab_user.csv', 'r') as fd:
        line = 'a'
        while line != '':
            line = fd.readline()
            line = line.strip()
            raw = line.split(',')
            print(raw)
            raw[-2], raw[-1] = raw[4].split()
            print(','.join(raw), file=fout)
