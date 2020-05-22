salary=int(input("Enter a salary : "))
yearOnJob=int(input("Enter years of experience : "))
if salary>=3000:
    if yearOnJob>=3 :
        print("You qualify for a loan :)")
    else:
        print("You qualify for a half a loan :) :)")
else:
    if yearOnJob>=10:
        print("You qualify for a half of a 25% of a loan")
    else:
        print("You do not qualify for loans")
