import re
import yaml

flights = []
row = ''
date = ''
plane = ''
fr = ''
status = ''
to = ''
first_line = 1
result_file = open('SkyTeam-Exchange.csv', 'w')
with open('SkyTeam-Exchange.yaml') as fileobject:
    writer = csv.writer(result_file, delimiter=",")
    for line in fileobject:
        yaml_line = yaml.safe_load(line)
        key = list(yaml_line.keys())[0]
        value = list(yaml_line.values())[0]
        if re.match(r"\d\d\d\d-\d\d-\d\d", key) and not value:
            date = key
        elif key != 'FF' and not value:
            plane = key
        elif key != 'FF' and key != 'FROM' and key != 'STATUS' and key != 'TO' and value:
            s = key+','+value['CLASS']+','+value['FARE']
            flights.append(s)
        elif key == 'FROM':
            fr = value
        elif key == 'STATUS':
            status = value
        elif key == 'TO':
            to = value
            for i in range(len(flights)):
                row = date+','+plane+','+flights[i]+','+fr+','+status+','+to+'\n'
                result_file.write(row)
                #print(row)
            flights = []
result_file.close()