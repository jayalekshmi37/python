import csv
import pandas
field=['rollno','name','age']
sdict=[{'rollno':1,'name':'Divya','age':30},{'rollno':2,'name':'Anu','age':35}]
with open("dept.csv","w")as dfile:
	writer=csv.DictWriter(dfile,fieldnames=field)
	writer.writeheader()
	writer.writerows(sdict)
data=pandas.read_csv("dept.csv")	
print(data)
