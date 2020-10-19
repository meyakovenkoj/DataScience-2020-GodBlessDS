# -*- coding: utf-8 -*-
import csv
from lxml import etree as et
import re
import yaml


#profile id = cardnumber
#flight id = flight id
idDict = dict()
j = 100000
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
flight_file.write('flightCode,Date,flight_id,Departure,Arrival\n')#,Class)
ticket_file.write('cardnumber,flight_id,Class\n')#


with open('PointzAggregator-AirlinesData.xml') as xml_data:
        xml = xml_data.read()
        root = et.fromstring(xml)

        #full dict
        for user_root in root.iter('user'):
            if len(list(user_root.iter('card'))) != 0:
                for card_root in user_root.iter('card'):
                    if len(list(card_root.iter('activity'))) != 0:
                        for activity_root in card_root.iter('activity'):
                            flightCode = activity_root.xpath("./Code/text()")[0]
                            Date = activity_root.xpath("./Date/text()")[0]
                            key = flightCode+Date
                            if(key in idDict):
                                flight_id = idDict[key]
                            else:
                                idDict[key] = j
                                flight_id = j
                                j += 1

with open('SkyTeam-Exchange.yaml') as yaml_data:
    for line in yaml_data:
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
                key2 = flightCode+date
                if(key2 in idDict):
                    flight_id = idDict[key2]
                else:
                    idDict[key2] = j
                    flight_id = j
                    j += 1
                flight_file.write(flightCode+','+date+','+str(flight_id)+','+from_+','+to+'\n')
                ticket_file.write(flights[i][0]+','+str(flight_id)+','+flights[i][1]+'\n')
                flight_file.flush()
                ticket_file.flush()

            flights = []
flight_file.close()
ticket_file.close()