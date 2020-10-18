with open('orig_data/process/out_oth.clean.csv', 'r') as fd:
    flight = []
    i = 0
    dic_fl = {}
    with open('orig_data/process/Sirena-export-fixed-flight.clean.csv', 'r') as inp:
        flight = inp.readlines()
        for each in flight:
            tmp = each.split(';')
            dic_fl[';'.join(tmp).strip()] = i
            i += 1
    line = 'a'
    while line != '':
        line = fd.readline()
        lst = line.split(';')
        if len(lst) > 10:
            fl = ';'.join(lst[1:9])
            print(fl)
            if dic_fl.get(fl, -1) != -1:
                nfl = str(dic_fl[fl]) + ';' + fl
                outline = lst[0] + ';' + \
                    str(dic_fl[fl]) + ';' + ';'.join(lst[9:])
                with open('orig_data/process/out_fl.csv', 'a') as fl_out:
                    print(nfl, file=fl_out)
                with open('orig_data/process/out_oth.csv', 'a') as oth_out:
                    print(outline, file=oth_out)
