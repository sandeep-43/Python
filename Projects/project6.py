#Student Name : Sandeep Singh
#Student ID : C0727422

import datetime
def read(f1,f2):
    month =0
    
    for line in f1.readlines()[1:]:
        month +=1
        temp = line.strip().split(",")
        if 200 <= int(temp[0]) <= 800 and int(temp[1])>0:
            allowed = int(temp[0])
            used = int(temp [1])
        else:
            allowed = "invalid"
            used = "invalid"
        calc(f2, month, allowed , used)
        
    
def calc(f2, month, allowed,used):
    if allowed != "invalid" and  used != "invalid":
        temp = used - allowed
        if temp>0:
            over = temp
            amount = 74.99 + over * .20
        else:
            over = 0
            amount = 74.99
    else :
        over = 0
        amount = 0

    out(f2, month, allowed, used, over, amount)

def out(f2, month, allowed, used, over, amount):
    
    f2.write("\n"+str(month)+"\t"+str(allowed)+"\t"+str(used)+"\t"+str(over)+"\t"+str(amount))
    
def main():
    f1 = open("PhoneBillInput.txt","r")
    f2 = open("PhoneBillOutput.txt","a")
    time = datetime.datetime.now()
    f2.write("    ****** Phone Bill *******\n")
    f2.write("***{}***\n".format(time))
    f2.write("\nMonth\tAllowed\tUsed\tOver\tAmount")
    read(f1,f2)
    f1.close()
    f2.close()
    
main()
