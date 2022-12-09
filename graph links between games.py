import csv
import copy
orignial_data = csv.reader(open("./result.csv"))

data = []
for line in orignial_data:
	data.append(line)
data_j = copy.deepcopy(data)
data_k = copy.deepcopy(data)
node_path ="game connection node.csv"
edge_path ="game connection edge.csv"

with open(node_path, 'w', newline='') as csvfile1:
	with open(edge_path, 'w', newline='') as csvfile2:
		name_company = {"Id","Label"}
		csv.writer(csvfile1).writerow(["Source","Target"])
		for i in data:
			name_company.add(i[0])
			for j in data_j:
				if i[2] == j[2] and i[0] != j[0]:
					csv.writer(csvfile2).writerow([i[0],j[0]])
			del data_j[0]
		csv.writer(csvfile1).writerow(["Id","Label"])
		temp = 0
		for i in name_company:
			csv.writer(csvfile1).writerow([temp, i])
			temp = temp+1





