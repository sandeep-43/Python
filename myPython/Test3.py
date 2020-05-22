
ch = 'y'
mydict = {}
while (ch=='y' or ch == 'Y'):
    key=input("Enter key : ")
    val = input ("Enter value : ")
    tempdict = {key : val}
    mydict.update(tempdict)
    print(mydict)
    #print("Do you want to enter more ? ")
    ch=input("Do you want to enter more ? ")
