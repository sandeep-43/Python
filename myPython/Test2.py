import time
mydict = {'Name' : 'Sandeep', 'Subject' : 'Python', 'RollNo' :1}
print(mydict)
print(mydict['Name'])
print(len(mydict))
print(type(mydict))
print(mydict.items())
#print(time.timezone())

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")


sortdict = sorted(mydict.items())
for k,v in sortdict:  
    print(sortdict)
