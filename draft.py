#program to print a list containing elements less than 10

l=list()

i= int(input("How many elements do you want to add in the list?"))

for a in range (i):
  a = int(input("Enter the elements"))
  
  if (a < 10):
    l.append(a)

  else:
    print("This element is out of range")

print("The final list is", l)
