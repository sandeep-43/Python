#Project 05 Question 1

import datetime

def inputPackages():
    while True:
        try:
            packages = int(input("\nEnter the number of packages purchased : "))
            break
        except :
            print("\nInvalid input format!!! Please re-enter an integer value")
    return packages

def calcAmount(packages):
    if packages <10:
        discount = 0
    elif packages >=10 and packages <=19:
        discount = .22
    elif packages >=20 and packages <=49:
        discount = .32
    elif packages >=50 and packages <=99:
        discount = .45
    else:
        discount = .55

    amount = (packages * 109) - (packages * discount)
    return amount, discount, packages

def output(amount, discount, packages):
    
    print("\n*****Billing Information*****")
    print("**",datetime.datetime.now(),"**")
    print("\nTotal packages purchased =",packages)
    print("Discount :", int(discount*100),"%")
    print("Amount : $" + str(amount))
    
def main():
    packages = inputPackages()
    amount, discount, packages = calcAmount(packages)
    output(amount, discount, packages)
    
main()
