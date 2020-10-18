import csv
import json


flight_id = 0
profile_id = 0
loyality_id = 0


def n(a):
    if a == None:
        return ''
    else:
        return str(a)


def print_airport(raw):
    out = ''
    out += n(raw['Airport']).upper() + ';' + \
        n(raw['City']) + ';' + n(raw['Country'])
    with open('orig_data/out/airports1.csv', 'a') as out_fd:
        print(out, file=out_fd)
    return n(raw['Airport']).upper()


def print_flight(raw):
    global flight_id
    out = ''
    tmp_fl = flight_id
    out += str(flight_id) + ';' + n(raw['Date']) + \
        ';' + n(raw['Codeshare']) + ';'
    out += print_airport(raw['Arrival']) + ';'
    out += print_airport(raw['Departure']) + ';'
    out += n(raw['Flight'])
    flight_id += 1
    with open('orig_data/out/flights.csv', 'a') as out_fd:
        print(out, file=out_fd)
    return tmp_fl


def print_loyality(raw):
    global profile_id
    global loyality_id
    out = ''
    out += str(loyality_id) + ';' + str(profile_id) + ';' + \
        n(raw['Status']) + ';' + \
        n(raw['programm']) + ' ' + n(raw['Number']).strip()
    loyality_id += 1
    with open('orig_data/out/loyality.csv', 'a') as out_fd:
        print(out, file=out_fd)


def print_profile(raw):
    global profile_id
    with open('orig_data/out/profile_fl.csv', 'a') as out_pr_fl:
        for each in raw['Registered Flights']:
            flight = print_flight(each)
            print(profile_id, flight, sep=';', file=out_pr_fl)
    out = ''
    out += str(profile_id) + ';' + n(raw['NickName']) + ';' + n(raw['Sex']) + ';' + \
        n(raw['Real Name']['Last Name']) + ';' + \
        n(raw['Real Name']['First Name'])
    with open('orig_data/out/profiles.csv', 'a') as out_pr:
        print(out, file=out_pr)
    for each in raw['Loyality Programm']:
        print_loyality(each)
    profile_id += 1


with open('orig_data/out/flights.csv', 'w') as out_fd:
    print('id;fl_date;codeshare;arrival;departure;flight_code', file=out_fd)
with open('orig_data/out/loyality.csv', 'w') as out_fd:
    print('id;pr_id;status;cardnumber', file=out_fd)
with open('orig_data/out/profile_fl.csv', 'w') as out_fd:
    print('pr_id;fl_id', file=out_fd)
with open('orig_data/out/profiles.csv', 'w') as out_fd:
    print('id;nickname;sex;last_name;first_name', file=out_fd)
with open('orig_data/out/airports1.csv', 'w') as out_fd:
    print('code;city;country', file=out_fd)


with open('orig_data/FrequentFlyerForum-Profiles.json', 'r') as fd:
    input = fd.read()
    input = json.loads(input)
    for each in input['Forum Profiles']:
        print_profile(each)
