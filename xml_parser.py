# -*- coding: utf-8 -*-
import csv
from lxml import etree as et
result_file = open('PointzAggregator-AirlinesData.csv', 'w', newline='')
writer = csv.writer(result_file, delimiter=",")
first_part = []
second_part = []
third_part = []
row = ['userid','firstname','lastname','cardstype','cardnumber','bonusprogramm',
'activitiesType','actType','actPlane','actDate','actDeparture','actArrival','actFare','Class']
writer.writerow(row)

with open('PointzAggregator-AirlinesData.xml') as xml_data:
    xml = xml_data.read()
    root = et.fromstring(xml)
    for user_root in root.iter('user'):
        first_part.clear()
        first_part.append(user_root.xpath("./@uid")[0])
        first_part.append(user_root.xpath("./name/@first")[0])
        first_part.append(user_root.xpath("./name/@last")[0])
        first_part.append(user_root.xpath("./cards/@type")[0])
        if len(list(user_root.iter('card'))) == 0:
            second_part.clear()
            second_part = ['NULL', 'NULL', 'NULL']
            third_part = ['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL']
            row = first_part + second_part + third_part
            #print(row)
            writer.writerow(row)
            result_file.flush()#force write from cache to file
        else:
            for card_root in user_root.iter('card'):
                second_part.clear()
                second_part.append(card_root.xpath("./@number")[0])
                second_part.append(card_root.xpath("./bonusprogramm/text()")[0])
                second_part.append(card_root.xpath("./activities/@type")[0])
                if len(list(card_root.iter('activity'))) == 0:
                    third_part.clear()
                    third_part = ['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL','NULL']
                    row = first_part + second_part + third_part
                    #print(row)
                    writer.writerow(row)
                    result_file.flush()
                else:
                    for activity_root in card_root.iter('activity'):
                        third_part.clear()
                        third_part.append(activity_root.xpath("./@type")[0])
                        third_part.append(activity_root.xpath("./Code/text()")[0])
                        third_part.append(activity_root.xpath("./Date/text()")[0])
                        third_part.append((activity_root.xpath("./Departure/text()")[0]).upper())
                        third_part.append((activity_root.xpath("./Arrival/text()")[0]).upper())
                        third_part.append(activity_root.xpath("./Fare/text()")[0])
                        third_part.append('NULL')#for Class
                        row = first_part + second_part + third_part
                        #print(row)
                        writer.writerow(row)
                        result_file.flush()

result_file.close()