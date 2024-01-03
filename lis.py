with open("stud.txt")as f:
	slist=f.readlines()
print(slist)
slist=[x.strip() for x in slist] 
print("Contents of the file are: ",slist)

