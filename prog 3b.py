# function to return second largest number from a list of numbers

def seclargestnum(list1):
  
  list1.sort()
  secondlast = list1[-2]
  
  return secondlast

list1 = [1,2,3,4,5,6,7,8,9]
secnum = seclargestnum(list1)

print("The elements of the list are", list1)
print("The second largest number of the list is", secnum)
