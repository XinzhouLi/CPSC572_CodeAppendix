import csv


edge = csv.reader(open("./edge_id.csv"))
namelist = csv.reader(open("./unique_name_list.csv"))
path = "cleaned name list.csv"
existedNodeId =[]
allNode =[]


for line in edge:
	if line[0] == "Source":
		continue
	existedNodeId.append(line[0])
	existedNodeId.append(line[1])
print(existedNodeId)
for line in namelist:
	allNode.append(line)
print(allNode)
with open(path, 'w', newline='') as csvfile:
	csv_write = csv.writer(csvfile)
	csv_write.writerow((["Id","Label"]))
	for i in allNode:
		if i[0] in existedNodeId:
			csv_write.writerow(i)
