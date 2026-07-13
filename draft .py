#program to print list with numbers less than 10

list1 = list()

a = int(input("How many elements do you want to add in the list?"))

for i in range(a):
  i = int(input("Enter the elements:"))
 
  if ( i < 10) :
    list1.append(i)
 
  else:
    print ("This number is out of range")

print (list1)
