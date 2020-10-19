# -*- coding: utf-8 -*-
import csv
from lxml import etree as et
users_file = open('XML_users.csv', 'w', newline='')#result_file
cards_file = open('XML_cards.csv', 'w', newline='')
flight_file = open('XML_flight.csv', 'w', newline='')
ticket_file = open('XML_ticket.csv', 'w', newline='')

users_writer = csv.writer(users_file, delimiter=",")
cards_writer = csv.writer(cards_file, delimiter=",")
flight_writer = csv.writer(flight_file, delimiter=",")
ticket_writer = csv.writer(ticket_file, delimiter=",")

users_row = ['userid','firstname','lastname']
cards_row = ['userid','cardnumber','bonusprogrammName']
flight_row = ['cardnumber','flightCode','Date','Departure','Arrival']#,'Class']
ticket_row = ['cardnumber', 'flightCode', 'Class']

users_writer.writerow(users_row)
cards_writer.writerow(cards_row)
flight_writer.writerow(flight_row)
ticket_writer.writerow(ticket_row)

with open('PointzAggregator-AirlinesData.xml') as xml_data:
    xml = xml_data.read()
    root = et.fromstring(xml)

    for user_root in root.iter('user'):
        users_row.clear()
        users_row.append(user_root.xpath("./@uid")[0])
        userid = user_root.xpath("./@uid")[0]#
        users_row.append(user_root.xpath("./name/@first")[0])
        users_row.append(user_root.xpath("./name/@last")[0])
        users_writer.writerow(users_row)
        users_file.flush()#force write from cache to file

        if len(list(user_root.iter('card'))) != 0:
            for card_root in user_root.iter('card'):
                cards_row.clear()
                cards_row.append(userid)
                cards_row.append(card_root.xpath("./@number")[0])
                cardnumber = card_root.xpath("./@number")[0]#
                cards_row.append(card_root.xpath("./bonusprogramm/text()")[0])
                cards_writer.writerow(cards_row)
                cards_file.flush()

                if len(list(card_root.iter('activity'))) != 0:
                    for activity_root in card_root.iter('activity'):
                        ticket_row.clear()#
                        flight_row.clear()
                        flight_row.append(cardnumber)
                        ticket_row.append(cardnumber)#
                        flight_row.append(activity_root.xpath("./Code/text()")[0])
                        ticket_row.append(activity_root.xpath("./Code/text()")[0])#
                        flight_row.append(activity_root.xpath("./Date/text()")[0])
                        flight_row.append((activity_root.xpath("./Departure/text()")[0]).upper())
                        flight_row.append((activity_root.xpath("./Arrival/text()")[0]).upper())
                        ticket_row.append('')#for Class
                        flight_writer.writerow(flight_row)
                        flight_file.flush()
                        ticket_writer.writerow(ticket_row)
                        ticket_file.flush()

users_file.close()
cards_file.close()
flight_file.close()