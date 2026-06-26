# program to write a function that returns largest element of the list passed as parameter
# this can be done in two ways, we will be doing the other of them here.

# using for loop to iterate every element and checking for the maximum value

def largestnum(list1):
  length = len(list1)
  num = 0

  for i in range(length):
  
    if (i == 0 or list1[i] > num):
      num = list1[i]
    
  return num

list1 = [1,2,3,4,5,6,7,8,9]
max_num = largestnum(list1)

print("The elements of the list:", list1)
print("The largest number of the list:", max_num)
