def addElements(list1):
	newList = list1
	inp = input ("Do you want to add any new element to the list? (Y/N)")
	
	if (inp == 'Y' or inp =='y'):
		elem = int(input("Enter the elements:"))
		index = int(input("Enter the index at which you would like to add the elements:"))
		newList.insert(index,elem)
		print("***Element added***")
		addElements(newList)
		return newList

list1 = []
inp = int(input("How many elements do you want to add in the list?"))

for i in range(inp):
	a = int(input("Enter the elements:"))
	list1.append(a)
	print ("The list entered is:", list1)

modList = addElements(list1)
print ("The modified list is:", modList)
