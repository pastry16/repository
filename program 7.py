#program to delete an element from desired position in a list
def deleteElements():
	global list1
	inp = input("Do you want to delete any element from the list? (Y/N)")
	if (inp == 'Y' or inp == 'y'):
		elem = int(input("Enter the element which you would like to delete:"))
	for a in list1:
		if (a == elem):
			list1.remove(elem)
			print ("The element is deleted from the list.")
			deleteElements()
		else:
			print("The element is in the list", list1)
		list1= []
		inp = int(input("How many elements do you want to add in the list?"))
		for i in range(inp):
			a = int(input("Enter the elements:"))
			list1.append(a)
			print("The list entered is:", list1)
			deleteElements()
						