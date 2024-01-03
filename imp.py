import csv
with open("stud1.csv","r")as efile:
	data=csv.reader(efile)
	for i in data:
		print(i)
