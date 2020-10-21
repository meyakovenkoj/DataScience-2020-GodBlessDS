# FROM: Jeddah , Saudi Arabia JED
# TO: Abha, Saudi Arabia AHB
# Validity Days Dep
# Time
# Arr
# Time
# Flight Aircraft Travel
# Time
# 01 Nov - 31 Jan 1234567 00:10 01:30 SV1670 320 1H20M
# 01 Nov - 31 Jan 1234567 00:40 02:00 SV1942 320 1H20M
# 01 Nov - 31 Jan 3 5 7 02:55 04:15 SV1664 EQV 1H20M
# 01 Nov - 31 Jan 1234567 04:25 05:45 SV1944 320 1H20M
# 01 Nov - 31 Jan 1234567 04:40 06:00 SV1650 320 1H20M
# 01 Nov - 31 Jan 1234567 05:25 06:45 SV1840 320 1H20M
# 01 Nov - 31 Jan 1234567 06:10 07:30 SV1656 320 1H20M
# 01 Nov - 31 Jan 1234567 10:40 12:00 SV1658 320 1H20M
# 01 Nov - 31 Jan 1234567 12:40 14:00 SV1666 320 1H20M

import re
from datetime import date, time

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def convert_time(str_time):
    res = re.search(r'(\d+)H(\d+)M', str_time)
    if res != None:
        return (int(res.group(1)) * 60 + int(res.group(2))) * 60
    else:
        return 0


def check_date(str_date):
    res = re.match(r'(\d{2})\s(\w{3})\s-\s(\d{2})\s(\w{2})', str_date)
    if res != None:
        if res.group(4) == months[0]:
            return date(2018, 
                        months.index(res.group(2)) + 1, 
                        int(res.group(1))), 
                   date(2019, 
                        months.index(res.group(4)) + 1, 
                        int(res.group(3)))
        return date(2018, 
                    months.index(res.group(2)) + 1, 
                    int(res.group(1))), 
               date(2018, 
                    months.index(res.group(4)) + 1, 
                    int(res.group(3)))


def check_week(str_week):
    res = re.search(r'-\s\d{2}\s\w{3}\s((\d|\s)+)\s\d{2}\:\d{2}', str_week)
    if res != None:
        return res.group(1)


def check_time(str_time):
    res = re.findall(r'(\d{2})\:(\d{2})(\+1)?', str_time)
    if res != []:
        # print(time(int(res[0][0]), int(res[0][1])),
        #       time(int(res[1][0]), int(res[1][1])))
        return time(int(res[0][0]), int(res[0][1])), time(int(res[1][0]), int(res[1][1]))


def get_flight_aircraft(str_all):
    res = re.search(
        r'\d{2}\:\d{2}(\+\-?\d)?\s((\d|\w|\*)+)\s((\d|\w)+)\s\d+H\d+M', str_all)
    if res != None:
        return res.group(2), res.group(4)


def check_airport(str_all):
    res = re.match(r'(^(FROM|TO):\s(.+)\s?,(.*)\s(...))', str_all)
    if res != None:
        return res.group(2), res.group(3).strip(), res.group(4).strip(), res.group(5)


# print(check_time('01 Nov - 31 Jan 1234567 12:40 14:00 SV1666 320 1H20M'))
# print(check_week('01 Nov - 31 Jan 1234567 12:40 14:00 SV1666 320 1H20M'))
# print(check_date('01 Nov - 31 Jan 1234567 12:40 14:00 SV1666 320 1H20M'))
# print(convert_time('01 Nov - 31 Jan 1234567 12:40 14:00 SV1666 320 1H20M'))
# print(get_flight_aircraft('01 Nov - 31 Jan 1234567 12:40 14:00 SV1666 320 1H20M'))
# print(check_airport('FROM: Jeddah , Saudi Arabia JED'))
# TO: Abha, Saudi Arabia AHB
# Validity Days Dep
# Time
# Arr
# Time
# Flight Aircraft Travel
# Time
# 01 Nov - 31 Jan 1234567 00:10 01:30 SV1670 320 1H20M
# 01 Nov - 31 Jan 1234567 00:40 02:00 SV1942 320 1H20M
# 01 Nov - 31 Jan 3 5 7 02:55 04:15 SV1664 EQV 1H20M
# 01 Nov - 31 Jan 1234567 04:25 05:45 SV1944 320 1H20M
# 01 Nov - 31 Jan 1234567 04:40 06:00 SV1650 320 1H20M
# 01 Nov - 31 Jan 1234567 05:25 06:45 SV1840 320 1H20M
# 01 Nov - 31 Jan 1234567 06:10 07:30 SV1656 320 1H20M
# 01 Nov - 31 Jan 1234567 10:40 12:00 SV1658 320 1H20M
# 01 Nov - 31 Jan 1234567 12:40 14:00 SV1666 320 1H20M'''))


def add_airport(dist, airports):
    if airports.get(dist[3], 0) == 0:
        airports[dist[3]] = (dist[1], dist[2])
    return dist[3]


if __name__ == "__main__":
    # line_count = 0
    airports = {}
    skip_list = ['Validity Days Dep', 'Time', 'Arr',
                 'Flight Aircraft Travel', 'Consult your travel agent for details', '', 'Operated by']

    from_id = 0
    to_id = 0
    with open('orig_data/out/skyteam_timetable.csv', 'w') as fout:
        print('from_id', 'to_id', 'from_date', 'til_date', 'week',
              'dep_time', 'arr_time', 'flight', 'aircraft', 'travel_time', sep=';', file=fout)
        with open('orig_data/SkyTeam_Timetable.txt', 'r') as fin:
            line = 'a'
            while line != '':
                line = fin.readline()
                # line_count += 1
                # print(line_count)
                if line.strip() not in skip_list and 'Operated by' not in line:
                    # print(line)
                    dist = check_airport(line)

                    if dist != None:
                        if 'FROM' in dist[0]:
                            from_id = add_airport(dist, airports)
                            continue
                        else:
                            to_id = add_airport(dist, airports)
                            continue
                    fdate = check_date(line)
                    week = check_week(line)
                    ftime = check_time(line)
                    flight_aircraft = get_flight_aircraft(line)
                    t_time = convert_time(line)
                    # print(line)
                    print(from_id, to_id, str(fdate[0]), str(fdate[1]), week,
                          str(ftime[0]), str(ftime[1]), flight_aircraft[0], flight_aircraft[1], t_time, sep=';', file=fout)
    with open('orig_data/out/airports.csv', 'w') as fout:
        print('code', 'city', 'country', sep=';', file=fout)
        for each in airports.keys():
            print(each, airports[each][0], airports[each]
                  [1], sep=';', file=fout)
