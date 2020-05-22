weight = float(input("How many pounds does your suitcase weigh? "))
if weight < 50:
    print("There is a $25 charge for luggage that heavy.")

elif 51< weight <100:
    print ("There is $50 extra charge for luggage that heavy.")
else:
    print("Please send this luggage as cargo!!!")
print("Thank you for your business.")
