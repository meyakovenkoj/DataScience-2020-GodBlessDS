import re
import yaml

flights = []
flight = []
row = ''
date = ''
flightCode = ''
fr = ''
status = ''
to = ''
first_line = 1
flight_file = open('YAML_flight.csv', 'w')
flight_row = []
flight_file.write('cardnumber,flightCode,Date,Departure,Arrival,Fare,Class\n')
with open('SkyTeam-Exchange.yaml') as fileobject:
    for line in fileobject:
        yaml_line = yaml.safe_load(line)
        key = list(yaml_line.keys())[0]
        value = list(yaml_line.values())[0]
        if re.match(r"\d\d\d\d-\d\d-\d\d", key) and not value:
            date = key
        elif key != 'FF' and not value:
            flightCode = key
        elif key != 'FF' and key != 'FROM' and key != 'STATUS' and key != 'TO' and value:
            flight.clear()
            flight.append(key)
            flight.append(value['FARE']) 
            flight.append(value['CLASS'])
            flights.append(flight)
        elif key == 'FROM':
            from_ = value.upper()
        elif key == 'TO':
            to = value.upper()
            for i in range(len(flights)):
                row = flights[i][0]+','+flightCode+','+date+','+from_+','+to+','+flights[i][1]+','+flights[i][2]+'\n'
                flight_file.write(row)
            flights = []
flight_file.close()