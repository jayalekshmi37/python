list1=[12, 45, 2, 41, 31, 10, 8, 6, 4,4,12]
def find_len(list1):
	length = len(list1)
	list1.sort()
	print("Largest element is:", list1[length-1])
	print("Smallest element is:", list1[0])
Largest = find_len(list1)
def Remove(list1):
	final_list = []
	for num in list1:
		if num not in final_list:
			final_list.append(num)
	return final_list
print("Before removing: ",list1)
print("After removing duplicate elements: ")	
print(Remove(list1))
result = []
l2=[0,7]
for ele in list1:
    result.append(ele)
    result.append(l2)
print(result)
