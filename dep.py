import csv
with open('dep.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID Department Name")
 print("---------------------------------")
 for row in data:
   print(row['department_id'], row['department_name'])
