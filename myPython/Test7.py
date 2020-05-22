nestedList=[]
lst=[]


for i in range(0,3):
    for j in range(0,3):
        itm = int(input("Enter into a list : "))
        
        lst.append(itm)
    temp= list(lst)
    nestedList.append(temp)
    print(nestedList)
    lst.clear()
    
    


#print(nestedList)

