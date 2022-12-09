import csv
csv_result = csv.reader(open("./result.csv"))

path = "people knowing others.csv"
re = []
with open(path, 'w', newline='') as csvfile:
	csv_write = csv.writer(csvfile)
	for line in csv_result:
		re.append(line)
	for i in re:
		for j in re:
			if i[0] == j[0] and not i[2] == j[2]:
				if i[1] == j[1] or (i[1] == "Production" or i[1] == "Design"):
					csv_write.writerow([i[2],j[2]])