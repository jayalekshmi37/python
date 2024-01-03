sfile=open("stud.txt","r")
efile=open("even.txt","w")
ofile=open("odd.txt","w")
content=sfile.readlines()
print("Contents of the files are: ",content)
for i in range(len(content)):
	if(i%2==0):
		efile.w(content[i])
	else:
		ofile.w(conent[i])
