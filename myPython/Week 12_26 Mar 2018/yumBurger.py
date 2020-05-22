#Yum Yum Burger Joint

#the main function
def main():
    endProgram = 'no'
    print()
    while endProgram == 'no':
        totalBurger = 0
        totalFry = 0
        totalSoda = 0
        total = 0
        endOrder = 'no'

        while endOrder == 'no':
            print()
            print ('Enter 1 for Yum Yum Burger')
            print ('Enter 2 for Grease Yum Fries')
            print ('Enter 3 for Soda Yum')
            option = input('Enter now ->')
            if option == '1':
                totalBurger = getBurger(totalBurger)
            elif option == '2':
                totalFry = getFry(totalFry)
            elif option == '3':
                totalSoda = getSoda(totalSoda)
            else:
                print ('You have entered an invalid option!!!')
            endOrder = input('Do you want to end your order? (Enter yes or no): ')
        print()
        #total = totalBurger + totalFry + totalSoda
        total = calcTotal(totalBurger, totalFry, totalSoda)
        printReceipt(total)
        endProgram = input('Do you want to end program? (Enter no to process a new order): ')

#this function will get burger order
def getBurger(totalBurger):
    burger = int(input("How many yum burgers ? "))
    totalBurger = totalBurger + burger * .99
    return totalBurger
    
#this function will get fry order
def getFry(totalFry):
    fry = int(input("How many Grease Yum Fries? "))
    totalFry = totalFry + fry * .79
    return totalFry

def getSoda(totalSoda):
    soda = int(input("How many Soda Yum? "))
    totalSoda = totalSoda + soda * 1.09
    return totalSoda
    
def calcTotal(totalBurger, totalFry, totalSoda):
    #subTotal = 0
    subTotal = totalBurger + totalFry + totalSoda
    taxes = subTotal * .06
    total = subTotal + taxes
    return total
               

def printReceipt(total):
    print ('The total price is $', total)

# calls main
main()
