with open('orig_data/process/BoardingData.csv', 'r') as fd:
    users = []
    i = 0
    dic_usr = {}
    with open('orig_data/process/pass_from_csv.csv', 'r') as inp:
        users = inp.readlines()
        for each in users:
            tmp = each.split(';')
            dic_usr[';'.join(tmp).strip()] = i
            i += 1
    line = 'a'
    while line != '':
        line = fd.readline()
        lst = line.split(';')
        usr = ';'.join(lst[:6])
        # print(dic_usr.get(usr, -1))
        if dic_usr.get(usr, -1) != -1:
            nusr = str(dic_usr[usr]) + ';' + usr
            outline = str(dic_usr[usr]) + ';' + ';'.join(lst[6:])
            with open('orig_data/process/out_usr.csv', 'a') as usr_out:
                print(nusr, file=usr_out)
            with open('orig_data/process/out_oth.csv', 'a') as oth_out:
                print(outline, file=oth_out)
