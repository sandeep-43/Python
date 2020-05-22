sales=int(input("Enter sales for the current month : "))
sales_perc = int(input("Enter sales %age : "))
if sales>90000 and sales_perc >125:
    print("Congrats!!! You'll get a day off")
    if sales>=100000:
        storebonus = 5000
        print("Store bonus : ",storebonus)
    elif sales>=150000:
        storebonus = 5500
        empbonus = 100
        print("Store bonus : ",storebonus)
        print("Employee bonus : ",empbonus)
else:
    print("Ordinary sales this month as well !!!")
    
