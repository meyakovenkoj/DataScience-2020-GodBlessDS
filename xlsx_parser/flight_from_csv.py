import re
import os
from os import listdir
os.getcwd()
if __name__ == "__main__":
	with open('orig_data/csv_oth_clean.csv', 'r') as fin:
		line = fin.readline()
		with open('orig_data/out/flight_from_csv.csv', 'w') as fout:
			while line != '':
						line_arr = re.split(';', line)
						print(line_arr[0], line_arr[4], line_arr[5], line_arr[6], line_arr[8], sep=';', file=fout)
						line = fin.readline()
		

