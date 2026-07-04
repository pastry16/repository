# program to store information of your friends

dic = {}

while True: 
  print("1. Add new contact")
  print("2. Modify phone number of contact")
  print("3. Delete a friend's contact")
  print("4. Display all entries")
  print("5. Check if a friend is present or not")
  print("6. Display in sorted order of names")
  print("7. Exit")

inp = int(input("Enter your choice (1-7):"))

if (inp == 1): 
  name = input ("Enter your friend's name:")
  phonenumber = input("Enter your friend's contact number:")
  dic[name] = phonenumber
  print("Contact Added \n\n")

elif (inp == 2):
  name = input ("Enter the name of friend whose number is to be modified: ")
  if (name in dic):
    phonenumber = input("Enter the new contact number: ")
    dic[name] = phonenumber
    print("Contact modified \n\n")

  else:
    print("This friend's name is not present in the contact list")

elif (inp == 3):
  name = input ("Enter the name of friend whose contact is to be deleted")
  if (name in dic):
    del dic [name]
    print("Contact Deleted \n\n")

  else:
    print ("This friend's name is not present in the contact list")

elif (inp == 4):
  print ("All entries in the contact")
  for a in dic:
    print ( a , "\t\t" , dic[a])
    print ("\n\n\n")

elif (inp == 5):
  name = input("Enter the name of friend to search:")
  if (name in dic):
    print ("The friend",name,"is present in the list \n\n" )
  else:
    print ("The friend",name, "is not present in the list \n\n")

elif (inp == 6):
  print("Name \t\t\t Contact number")
  for i in sorted(dic.keys()):
    print ( i, "\t\t\t" , dic[i])
    print ("\n\n")

elif (inp == 7):
  break
else:
  print("Invalid choice. Please try again \n")

