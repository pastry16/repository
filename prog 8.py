# program to find highest 2 values in a dictionary

dic = {"A":12,"B":13,"C":9,"D":89,"E":34,"F":17,"G":65,"H":36,"I":25,"J":11}
list1 = list()

for a in dic.values():
  list1.append(a)

list1.sort()  

print ("Highest value is", list1[-1])
print ("Second highest value is", list1[-2])
