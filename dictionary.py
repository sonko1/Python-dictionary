#Creating and printing a dictionary and learning several methods used in dictionary.
student = {
  "name": "Gabriel",
  "email": "gabrielkyalombuvi@gmail.com",
  "phone_no":706270437,
  "year": 1992
}
print(student)
#Accessing Item
x=student['email']
print(x)
print(student['name'])
#Get () the value of the "email" key
y=student.get('email')
print(y)
#Get () the value of the "year" key
z=student.get('year')
print(z)
#change values
student['name']="steve"
print(student)
#factoring to single line
print(student['name'])
#loop through a dictionary
for s in student:
  print(s)
  #values
  for value in student.values():
    print(value)
#Items () in accessing both values and keys
for k, v in student.items():
  print(k,v)
  #heck if "name" is present in the dictionary
  if "name" in student:
    print('name is there')
#Check if "model" is present in the dictionary
    if "model" in student:
     print('name is there ')
else:
       print('not there')
#Adding Reg No: an item to the dictionary
student["Reg NO:"] = "BSCIT-01-0382/2019"
print(student)
#Adding My Identity: an item to the dictionary
student["ID:"]="31440657"
print(student)
#Adding Maritual status: an item to the dictionary
student["Status:"]="complicated"
print(student)
#Removing status using pop() from dictionary
student.pop('Status:')
print(student)
#determine how many items in a dictionary
print(len(student))
#Make a copy of a dictionary with the copy() method
mydict = student.copy()
print(mydict)
#The update() method inserts the specified items to the dictionary.
student.update({"name:": "White:"})
print(student)
#The setdefault() method returns the value of the item with the specified key.
x = student.setdefault("Status:", "Sonko:")
print(x)
#Popitem() method removes the item that was last inserted into the dictionary
student.popitem()
print(student)