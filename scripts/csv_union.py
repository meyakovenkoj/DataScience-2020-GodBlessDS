def prep_airports():
    airports = dict()
    with open('orig_data/out/airports.csv', 'r') as pdf_out:
        for each in pdf_out.readlines():
            each = each.strip()
            airport_code = each.split(';')[0].upper()
            each = airport_code + each[3:]
            if airports.get(airport_code, -1) == -1:
                airports[airport_code] = each
            elif airports[airport_code] != each:
                print("COLLISION", '"' + each + '"',
                      '"' + airports[airport_code] + '"')

    print('JSON')
    with open('orig_data/out/airports1.clean.csv', 'r') as json_out:
        for each in json_out.readlines():
            each = each.strip()
            airport_code = each.split(';')[0].upper()
            each = airport_code + each[3:]
            if airports.get(airport_code, -1) == -1:
                airports[airport_code] = each
            elif airports[airport_code] != each:
                print("COLLISION", '"' + each + '"',
                      '"' + airports[airport_code] + '"')
    with open('orig_data/out/airports_union.csv', 'w') as out:
        print('code;city;country', file=out)
        keys = list(airports.keys())
        for each in sorted(keys):
            print(airports[each], file=out)
    # print(airports)


prep_airports()
