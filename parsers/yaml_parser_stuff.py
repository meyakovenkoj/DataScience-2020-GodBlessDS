import re
import yaml

flights = []
flight = []
date = ''
flightCode = ''
fr = ''
status = ''
to = ''
first_line = 1
flight_file = open('YAML_flight.csv', 'w')
ticket_file = open('YAML_ticket.csv', 'w')

#profile id = cardnumber
#flight id = flight id
flight_file.write('flightCode,Date,Departure,Arrival\n')#,Class)
ticket_file.write('cardnumber,flightCode,Date,Class\n')#
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
            #flight.append(value['FARE']) 
            flight.append(value['CLASS'])
            flights.append(flight)
        elif key == 'FROM':
            from_ = value.upper()
        elif key == 'TO':
            to = value.upper()
            for i in range(len(flights)):
                flight_file.write(flightCode+','+date+','+from_+','+to+'\n')
                ticket_file.write(flights[i][0]+','+flightCode+','+date+','+flights[i][1]+'\n')
                flight_file.flush()
                ticket_file.flush()

            flights = []
flight_file.close()
ticket_file.close()