f2 = open("file1.txt", "r+")
#try r+ and with no mode specified, try also after deleting the file1
strg=f2.read(50)
print (" The sring is: ", strg,"\n")
# Close opened file
f2.close()
