f2 = open("file1.txt", "r") #try r+ and with no mode specified, try also after deleting the file1
strg=f2.read(50)
print (" The sring is: ", strg,"\n") # Close opened file f2.close()
# Writing to an existing file
f1 = open("file1.txt", "w")
f1.write("Thanks for contacting us.")
print ("The name of the file is: ", f1.name)
print ("File closed : ", f1.closed)
print ("The opening mode is : ", f1.mode)

f1.close()
print ("File closed : ", f1.closed)
