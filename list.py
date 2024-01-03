import csv
with open("item.csv",'r')as f:
 for i in f:
  data=csv.reader(f)
  print(i)
