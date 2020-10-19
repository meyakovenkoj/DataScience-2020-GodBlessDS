with open('orig_data/out/xlsx_oth.clean.csv', 'r') as fd:
    flight = []
    i = 0
    dic_fl = {}
    with open('orig_data/out/flight_from_xlsx_clean.csv', 'r') as inp:
        flight = inp.readlines()
        for each in flight:
            tmp = each.split(';')
            dic_fl[';'.join(tmp).strip()] = i
            i += 1
    line = 'a'
    while line != '':
        line = fd.readline()
        lst = line.split(';')
        if len(lst) > 2:
            fl = ';'.join(lst[2:8])
            print(fl)
            if dic_fl.get(fl, -1) != -1:
                nfl = str(dic_fl[fl]) + ';' + fl
                outline = lst[0] + ';' + \
                    str(dic_fl[fl]) + ';' + ';'.join(lst[0:1]) + ';'.join(lst[11:12])
                with open('orig_data/out/flight_xlsx_id.csv', 'a') as fl_out:
                    print(nfl, file=fl_out)
                with open('orig_data/out/ticket_xlsx_id.csv', 'a') as oth_out:
                    print(outline, file=oth_out)
