#program to find the number of time an element occurs in the list.

list1 = [10,20,30,40,50,60,20,50,10,30,50,30,24,45]

print ("The list is:", list1)

inp = int(input("Which element occurence would you like to count?"))

count = list1.count(inp)

print("The count of element", inp, "in the list is:", count)
