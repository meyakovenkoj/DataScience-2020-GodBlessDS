import xlrd
import re
import os
from os import listdir
os.getcwd()
path='orig_data\BoardingPass/'
if __name__ == "__main__":
	with open('orig_data\out\Parsed_xlsx.csv', 'w') as fout:
		print('PassengerFirstName','PassengerSecondName','PassengerLastName','PassengerSex','TicketNumber','FlightNumber','FlightDate','FlightTime','Destination','From','DestinationAbr','FromAbr','PNR','Seat','Sequence','PassClass', sep=';', file=fout)
		for f in listdir(path):
			wb=xlrd.open_workbook(path+f,on_demand = True) #open xlsx file
			for sh in wb.sheets(): #work with the xlsx sheet
				PassengerSecondName = ''
				tmpname = sh.cell(2,1).value # temp variable for work with passenger's name cause it has bad format
				tmp_name_arr = re.split(' ', tmpname) # it can has two or three words
				tmp_name_arr.sort(key = lambda s: len(s)) #we have second_name only of one letter, so it'll be on first place
				if len(tmp_name_arr)==3:
					PassengerFirstName = tmp_name_arr[1]
					PassengerSecondName = tmp_name_arr[0] # second name if it is present
					PassengerLastName = tmp_name_arr[2]
				else:
					PassengerLastName = tmp_name_arr[1]
					PassengerFirstName = tmp_name_arr[0]
				PassengerSex = sh.cell(2,0).value
				TicketNumber = sh.cell(12,4).value
				FlightNumber = sh.cell(4,0).value
				FlightDate = sh.cell(8,0).value
				FlightTime = sh.cell(8,2).value
				Destination = sh.cell(4,7).value
				From = sh.cell(4,3).value
				DestinationAbr = sh.cell(6,7).value
				FromAbr = sh.cell(6,3).value
				PNR = sh.cell(12,1).value
				Seat = sh.cell(10,7).value
				Sequence = sh.cell(0,7).value
				PassClass = sh.cell(2,7).value
				print(PassengerFirstName,PassengerSecondName,PassengerLastName,PassengerSex,TicketNumber,FlightNumber,FlightDate,
				FlightTime,Destination,From,DestinationAbr,FromAbr,PNR,Seat,Sequence,PassClass, sep=';', file=fout)




				
			wb.release_resources()


