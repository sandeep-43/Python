# Appending to the file1.txt. The output : Thanks for contacting us. We are in the Python class,
#now. #Please, call again.
f1 = open("file1.txt", "a+")
f1.write(" We are in the Python class, now.\n Please, call again.\n Thanks.")
print ("The name of the file is: ", f1.name)
print ("File closed : ", f1.closed)
print ("The opening mode is : ", f1.mode)

f1.seek(0)

print("Reading now : \n",f1.read(50))
f1.close()
