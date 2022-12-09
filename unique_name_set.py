import csv


unique_set = {"id","name"}
csv_reader = csv.reader(open("./result.csv"))
path = "unique_name_list.csv"
id = 0
with open(path, 'w', newline='') as csvfile:
	csv_write = csv.writer(csvfile)
	csv_head = ["Name"]
	csv_write.writerow(csv_head)
	for line in csv_reader:
		unique_set.add(line[2])
	for i in list(unique_set):
		csv_write.writerow([id, i])
		id = id +1

print(unique_set)
