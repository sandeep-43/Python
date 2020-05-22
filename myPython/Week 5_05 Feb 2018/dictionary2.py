dict1= {'Name':'Sandeep', 'Age': '25'}
dict2= {'Name':'Amal', 'Age':24}

mySubTuple = ('October',2016,2.5)
print(len(dict1))
print(dict1 != dict2)
print(str(dict1))
print(dict1)
print(type(dict1))
print(type(mySubTuple))
print(dict1.keys())
print(dict1.values())
dict1.update(dict2)
print(dict1)
dict3=dict1.copy()
print(dict3)
print(dict2.get('Age'))
