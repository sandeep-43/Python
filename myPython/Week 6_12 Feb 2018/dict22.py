
#!/usr/bin/python3
dict1 = {'Name': 'Fahim', 'Age': 7}
dict2 = {'Name': 'Rana', 'Age': 7}
dict3 = {'tel': ' 9999889','Sex':'m'}
dict5= {'Name': 'Fahim', 'Age': 37, 'Tel':'555555','Address':'55 Main St.'}
mySubTuple = ('October', 2016, 21.5)
print (len (dict1))
print (dict1 != dict2)
print (str(dict1))
print (dict1)
print (type (dict1))
print (type (mySubTuple))
print (dict1.keys())
print (dict1.values())
print ("dict1 items: ",dict1.items())
item =list(dict1.items())
print ("list of items: ", item)
print (item[0][1])
dict1.update(dict3)
print (dict1)
dict4 = dict1.copy()
print (dict4)
print (dict2['Age'])#returns the value of Age, if not found an error is generated
#print (dict2['title'])
print (dict2.get('Ba'))# return the value of Age, if not found, it returns none
#print (dict2.get('title'))
dict3.setdefault('Sex', 'f')
dict3.setdefault('tel', None)#adding a key of tel with none value if tel is not found, otherwise it returns tel and its existing value
dict2.setdefault('Age', None)
print (dict3)
print (dict2)
