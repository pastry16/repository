#lists containing positive and negative elements

list1 = list()

inp = int(input("How many elements do you want to add in the list?(Element can be both positive and negative)"))

for i in range(inp):
  a = int(input("Enter the elements:"))
  list1.append(a)
print("The list with all the elements:", list1)

list2 = list()
list3 = list()

for j in range(inp):
 
  if list1[j] < 0:
    list3.append(list1[j])
  
  else: 
    list2.append(list1[j])

print("The list with positive elements:", list2) 
print("The list with negative elements:", list3)

