#This program takes inputs, calculates gross and net pays and then outputs the results
#payRate = 29
#hours = 40
#tax = 13.5
#empName = "Sandeep"
#payRate, hours, tax, empName = 29,40,13.5,"Sandeep"
payRate = input ("Enter payRate : ")
payRateConv = int(payRate)
hours = input ("Enter Hours : ")
hoursConv = int(hours)
tax = input ("Enter tax : ")
taxConv = int(tax)
empName = input ("Enter name : ")
grossPay = payRateConv * hoursConv
netPay = grossPay -(grossPay * taxConv/100)
print ("The pay rate is : ", payRate, "\nThe deducted tax is :", tax,"%", "\nThe grossPay is :", grossPay, "\nThe net pay is :", netPay, "\nThe employee name is :", empName)
#print ("The pay rate is ", payRate)
#print (""The deducted tax is ", tax,"%")