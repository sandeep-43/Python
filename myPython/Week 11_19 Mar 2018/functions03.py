localVal=9

def main():
    print("Welcome to the program")
    monthlySales = getSales()

    #Funtion to call determine bonus
    isBonus(monthlySales)

    #Function call to detemine day off
    isDayOff(monthlySales)
    


def getSales():
    #localVal = 9
    monthlySales = float(input("Enter the sales in $"))
    return monthlySales

def isBonus(monthlySales):
    if monthlySales >= 100000:
        print("You have earned a $5000 bonus!!!",localVal)

def isDayOff(monthlySales):
    if monthlySales>=125000:
        print("All employees get a day off!!!")
main()
