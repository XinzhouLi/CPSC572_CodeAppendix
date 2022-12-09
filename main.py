import csv

import numpy
import numpy as np
import pandas as pd

csv_reader = csv.reader(open("./572.csv"))
path = "result.csv"
unique_name = {}
with open(path, 'w', newline='') as csvfile:
	csv_write = csv.writer(csvfile)
	csv_head = ["Game Name", "Position", "Name"]
	csv_write.writerow(csv_head)
	for line in csv_reader:
		if line[1] == "" and line[2] == "" and line[3] == "" and line[4] == "" and line[5] == "" and line[6] == "":
			continue
		if not (line[1] == "" or line[1] == " "):
			produlist = line[1].split(',')
			for i in produlist:
				name = i.replace(u'\xa0', u' ')
				name = name.lstrip()
				name = name.rstrip()
				temp = [line[0], "Production", name]
				csv_write.writerow(temp)
		if not (line[2] == "" or line[2] == " "):
			produlist = line[2].split(',')
			for i in produlist:
				name = i.replace(u'\xa0', u' ')
				name = name.lstrip()
				name = name.rstrip()
				temp = [line[0], "Design", name]
				csv_write.writerow(temp)
		if not (line[3] == "" or line[3] == " "):
			produlist = line[3].split(',')
			for i in produlist:
				name = i.replace(u'\xa0', u' ')
				name = name.lstrip()
				name = name.rstrip()
				temp = [line[0], "Programming", name]
				csv_write.writerow(temp)
		if not (line[4] == "" or line[4] == " "):
			produlist = line[4].split(',')
			for i in produlist:
				name = i.replace(u'\xa0', u' ')
				name = name.lstrip()
				name = name.rstrip()
				temp = [line[0], "Art/Graph", name]
				csv_write.writerow(temp)
		if not (line[5] == "" or line[5] == " "):
			produlist = line[5].split(',')
			for i in produlist:
				name = i.replace(u'\xa0', u' ')
				name = name.lstrip()
				name = name.rstrip()
				temp = [line[0], "Audio", name]
				csv_write.writerow(temp)
		if not (line[6] == "" or line[6] == " "):
			produlist = line[6].split(',')
			for i in produlist:
				name = i.replace(u'\xa0', u' ')
				name = name.lstrip()
				name = name.rstrip()
				temp = [line[0], "Writer", name]
				csv_write.writerow(temp)


