#Student Name : Sandeep Singh
#Student ID : C0727422

import datetime

def getMeal():
    mealPrice = float(input("Enter the price of the meal in $:"))
    return mealPrice

def calcTaxes(mealPrice):
    if mealPrice >= .01 and mealPrice <= 5.99:
        tip = mealPrice * .10
    elif mealPrice >= 6 and mealPrice <=12:
        tip = mealPrice * .13
    elif mealPrice >=12.01 and mealPrice <=17:
        tip = mealPrice * .16
    elif mealPrice >= 17.01 and mealPrice <=25:
        tip = mealPrice * .19
    else:
        tip = mealPrice * .22

    tax = mealPrice * .06
    total = mealPrice + tip + tax
    return tax,tip,total

def printMealPrice(mealPrice,tax,tip,total):
    print("\n***** Billing Information *****")
    print("**",datetime.datetime.now(),"**")
    print("\nMeal price : $"+str(mealPrice))
    print("Tip : $"+str(tip))
    print("Taxes : $"+str(tax))
    print("Total expenses : $"+str(total))

def main():
    mealPrice = getMeal()
    tax,tip,total = calcTaxes(mealPrice)
    printMealPrice(mealPrice,tax,tip,total)
    
main()
