import re
import yaml

flights = []
row = ''
date = ''
flightCode = ''
fr = ''
status = ''
to = ''
first_line = 1
result_file = open('SkyTeam-Exchange.csv', 'w')
result_file.write('Date,flightCode,cardnumber,Class,Fare,Departure,Arrival\n')
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
            s = key+','+value['CLASS']+','+value['FARE']
            flights.append(s)
        elif key == 'FROM':
            fr = value.upper()
        elif key == 'TO':
            to = value.upper()
            for i in range(len(flights)):
                row = date+','+flightCode+','+flights[i]+','+fr+','+to+'\n'
                result_file.write(row)
                #print(row)
            flights = []
result_file.close()