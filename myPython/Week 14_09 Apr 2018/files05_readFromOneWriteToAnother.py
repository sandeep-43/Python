f14 = open("file1.txt","r")
f15 =open("file2.txt","w")

for k in f14:
    print(k.rstrip())
    f15.write(k)

f14.close()
f15.close()
