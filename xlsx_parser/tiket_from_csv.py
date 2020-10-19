import re
import os
from os import listdir
os.getcwd()
if __name__ == "__main__":
	with open('orig_data/csv_oth_clean.csv', 'r') as fin:
		line = fin.readline()
		with open('orig_data/out/ticket_from_csv.csv', 'w') as fout:
			while line != '':
						line_arr = re.split(';', line)
						print(line_arr[0], line_arr[1], line_arr[2], line_arr[3], sep=';', file=fout)
						line = fin.readline()
		

