f1 = open("file1.txt","r")
f2 = open("file2.txt","a")
for temp in f1.readlines():
    f2.write(temp)
    print(temp)
#for t in temp:
#    f2.write(t)
f1.close()
f2.close()
