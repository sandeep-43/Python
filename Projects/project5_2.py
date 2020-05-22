#Student Name : Sandeep Singh
#Student ID : C0727422

#months and days count are taken to be 3 each for demonstration purpose
def inputSales():
    m=0
    monthSales = []
    daysSales = []
    temp = []
    while m<3:
        for d in range(0,3):
            daysSales_temp = float(input("Enter sales for day {}, month {} : ".format(d+1,m+1)))
            daysSales.append(daysSales_temp)
        temp = list(daysSales)
        monthSales.append(temp)
        daysSales.clear()
        m+=1
        print()
    return monthSales

def average(monthSales):
    totalMonthlyAverage = []
    sumAverageEachMonth = 0
    m = 0
    while m<3:
        sumAverageEachMonth = sumAverageEachMonth + sum(monthSales[m])/len(monthSales[m])
        yearlyAverage = sumAverageEachMonth/3
        monthlyAverage = sum(monthSales[m])/len(monthSales[m])
        totalMonthlyAverage.append(monthlyAverage)
        print("Average sales for the month {} :".format(m+1),monthlyAverage)                                                     
        m+=1
    #return yearlyAverage, monthlyAverage
    print("Average yearly sales : ",yearlyAverage)

def total(monthSales):
    overallMonthlyTotal = []
    m = 0
    yearlyTotal = 0
    while m<3:
        yearlyTotal = yearlyTotal + sum(monthSales[m])
        monthlyTotal = sum(monthSales[m])
        overallMonthlyTotal.append(monthlyTotal)
        print("Total sales for the month {} :".format(m+1),monthlyTotal)                                                     
        m+=1
    #return yearlyTotal, overallMonthlyTotal
    print("Total yearly sales :",yearlyTotal)

def calcMax(monthSales):
    m=0
    print("Month\tDay\tHighestSales($)")
    while m<3:
        monthlyHigh = max(monthSales[m])
        index = monthSales[m].index(monthlyHigh)
        print(str(m+1)+"\t"+str(index+1)+'\t'+str(monthlyHigh))
        m +=1
                                                
def main():
    
    monthSales = inputSales()
    #print(monthSales)
    print()
    average(monthSales)
    print()
    total(monthSales)
    print()
    calcMax(monthSales)
              
main()
