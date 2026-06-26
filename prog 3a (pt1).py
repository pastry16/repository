# program to write a function that returns largest element of the list passed as parameter
# this can be done in two ways, we will be doing one of them here.
# using max() function of the list

def largestnum(list1):
  l = max(list1)
  return l
  
list1 = [1,2,3,4,5,6,7,8,9]

max_num = largestnum(list1)

print("The elements of the list:", list1)
print("The largest number of the list:", max_num)
