mealprice = input('Enter the meal price $')
mealprice = float(mealprice)
if mealprice >= .01 and mealprice <= 5.99:
    tip = mealprice * .10
elif mealprice >= 6 and mealprice <=12:
    tip = mealprice * .13
elif mealprice >=12.01 and mealprice <=17:
    tip = mealprice * .16
elif mealprice >= 17.01 and mealprice <=25:
    tip = mealprice * .19
else:
    tip = mealprice * .22
tax = mealprice * .06
total = mealprice + tip + tax
print ('The meal price is $', mealprice)
print ('The tip is $', tip)
print ('The tax is $', tax)
print ('The total is $', total)
