list = {'Nabil':16,'Tanya':19}
print (list.items())#listing all elements of list dictionary
print()
search = int(input('enter the age you search for'))
for name, age in list.items():
	if age == search:#searching for a matching name
		print (name)
		break
	
else:print ('key is not found')
