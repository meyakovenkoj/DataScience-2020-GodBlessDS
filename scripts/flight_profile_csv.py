with open(r'orig_data/process/csv_oth.clean.csv', 'r') as fd:
    flight = []
    i = 0
    dic_fl = {}
    with open(r'orig_data/process/flight_from_csv_clean.csv', 'r') as inp:
        flight = inp.readlines()
        for each in flight:
            tmp = each.split(';')
            # print(';'.join(tmp).strip())
            dic_fl[';'.join(tmp).strip()] = i
            i += 1
    line = 'a'
    # print(dic_fl)
    while line != '':
        line = fd.readline()
        lst = line.split(';')
        if len(lst) > 2:
            fl = ';'.join(lst[4:7]) + ';' + lst[-1]
            # print(fl)
            fl = fl.strip()
            if dic_fl.get(fl, -1) != -1:
                print(fl)
                nfl = str(dic_fl[fl]) + ';' + fl
                outline = ';'.join(lst[0:4]) + ';' + \
                    str(dic_fl[fl])
                with open(r'orig_data/process/out_csv_fl.csv', 'a') as fl_out:
                    print('!')
                    print(nfl, file=fl_out)
                with open(r'orig_data/process/out_csv_oth.csv', 'a') as oth_out:
                    print(outline, file=oth_out)
