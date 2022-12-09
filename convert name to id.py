import csv

node = csv.reader(open("./unique_name_list.csv"))
edge = csv.reader(open("./people knowing others.csv"))

path = "edge_id.csv"
nodeId =[]
nodeName = []
edgelist =[]
for line in node:
	if line[0] == "Id":
		continue
	nodeId.append(line[0])
	nodeName.append(line[1])
for line in edge:
	if line[0] == "Source":
		continue
	edgelist.append(line)

print(len(edgelist))
with open(path, 'w', newline='') as csvfile:
	csv_write = csv.writer(csvfile)
	csv_write.writerow((["Source","Target"]))
	for i in edgelist:
		try:

			id1 = nodeId[nodeName.index(i[0])]
			id2 = nodeId[nodeName.index(i[1])]
			csv_write.writerow([id1, id2])
		except:
			print(i[1])