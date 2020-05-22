#Name : Sandeep Singh
#Student ID : C0727422

def billInput(months,year):
    bills = []
    
    for month in months:
        while True:
            try :
                tempBills = float(input("Enter energy bill for {}, {} : ".format(month,year)))
                bills.append(tempBills)
                break
            except ValueError:
                print("Invalid input!!! Please enter amount in float")
    return bills


def calc(beforeGreenBills,afterGreenBills):
    eachMonthDifference = []
    for month in range(0,12):
        tempDifference = beforeGreenBills[month] - afterGreenBills[month]
        eachMonthDifference.append(tempDifference)
    totalDifference = sum(beforeGreenBills) - sum(afterGreenBills)
    return eachMonthDifference, totalDifference


def minmax(beforeGreenBills,afterGreenBills,months):
    eachMonthDifference, totalDifference = calc(beforeGreenBills,afterGreenBills)
    print("\nMinimum value was observed in {}, 2017 : ${}".format(months[eachMonthDifference.index(min(eachMonthDifference))], min(eachMonthDifference)))
    print("Maximum value was observed in {}, 2017 : ${}".format(months[eachMonthDifference.index(max(eachMonthDifference))], max(eachMonthDifference)))
    

def fetchMonth(months,beforeGreenBills,afterGreenBills):
    eachMonthDifference, totalDifference = calc(beforeGreenBills,afterGreenBills)
    while True:
        checkSavings_temp = str(input("\nEnter the month for which you need to check the savings : "))
        if not checkSavings_temp.isalpha():
            print("Incorrect month format!!! Please re-enter a string value...")
        else:
            break
            
    checkSavings = checkSavings_temp[0].upper()+checkSavings_temp[1:]
    for month,i in zip(months,range(0,12)):
        if checkSavings == month:
            print("Savings in the month of {}, 2017 was ${}".format(month,eachMonthDifference[i]))
            break
    else:print("Invalid month name !!!")
            

    
def output(months,beforeGreenBills,afterGreenBills):
    path = "C://Users//Sandeep Singh//Desktop//savings.txt"
    file = open(path,"w+")
    
    print("\n-----Amount spent for the year 2016 i.e. before going green-----")
    file.write("-----Amount spent for the year 2016 i.e. before going green-----")
    for month,beforeGreenBills_eachMonth in zip(months,beforeGreenBills):
        print("Amount spent in {}, 2016 : ${}".format(month,str(beforeGreenBills_eachMonth)))
        file.write("\nAmount spent in {}, 2016 : ${}".format(month,str(beforeGreenBills_eachMonth)))

    print("\n-----Amount spent for the year 2017 i.e. after going green-----")
    file.write("\n\n-----Amount spent for the year 2017 i.e. after going green-----")
    for month,afterGreenBills_eachMonth in zip(months,afterGreenBills):
        print("Amount spent in {}, 2017 : ${}".format(month, str(afterGreenBills_eachMonth)))
        file.write("\nAmount spent in {}, 2017 : ${}".format(month, str(afterGreenBills_eachMonth)))
    eachMonthDifference, totalDifference = calc(beforeGreenBills,afterGreenBills)

    print("\n-----Monthly savings-----")
    file.write("\n\n-----Monthly savings-----")
    for month,pos in zip(months,range(0,12)):
        print("Savings in {}, 2017 : ${}".format(month, str(eachMonthDifference[pos])))
        file.write("\nSavings in {}, 2017 : ${}".format(month, str(eachMonthDifference[pos])))
    print("\nTotal Savings : $"+str(totalDifference))
    file.write("\n\nTotal Savings : $"+str(totalDifference))
    file.close()

    
def main():
    beforeGreenBills = []
    afterGreenBills = []
    ch ='y'
    months = ("January","February","March","April","May","June","July","August"\
              ,"September","October","November","December")
    print("-----Please enter the energy bill before going green (for year 2016)-----")
    beforeGreenBills=billInput(months,2016)

    print("\n-----Please enter the energy bill after going green (for year 2017)-----")
    afterGreenBills = billInput(months,2017)

    output(months,beforeGreenBills,afterGreenBills)    

    minmax(beforeGreenBills,afterGreenBills,months)

    while ch == 'y':
        fetchMonth(months,beforeGreenBills,afterGreenBills)
        ch=input("\nDo you want to search more ? (y/n)")
        if ch=='n':
            print("\n{}Thank You{}".format('*'*10,'*'*10))
main()
