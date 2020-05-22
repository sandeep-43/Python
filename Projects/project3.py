#Name : Sandeep Singh
#Student ID : C0727422

def inputSales(month):
    sales = float(input("Enter sales for the {} month : ".format(month)))
    return sales

def storeBonus(currentSales):
    if currentSales >= 110000 :
        storeBonus = 6000
    elif currentSales >= 100000 :
        storeBonus= 5000
    elif currentSales >= 90000 :
        storeBonus = 4000
    elif currentSales >= 80000 :
        storeBonus = 3000
    else:
        storeBonus = 500
        
    return storeBonus
        
def employeeBonus(currentSales,previousSales):
    percentage = currentSales-previousSales/previousSales*100

    if percentage >= 5 :
        empBonus = 75
    elif percentage >= 4:
        empBonus = 50
    elif percentage >= 3:
        empBonus = 40
    else :
        empBonus = 0
        
    return empBonus

def main():
    currentSales = inputSales("current")
    previousSales = inputSales("previous")
    print("Store Bonus : $" + str(storeBonus(currentSales)))
    print("Employee Bonus : $" + str(employeeBonus(currentSales,previousSales)))
main()

