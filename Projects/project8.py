
#Student Name : Sandeep Singh
#Student ID : C0727422

import datetime

def inputdata():
    distance = float(input("Enter distance to be travelled (nautical miles) : "))
    #distanceInKm = distance * 1.852
    return distance

def calc(distance):
    time = distance/120
    
    gas = (time+.5) * 8.4
    fuel = round(gas,1)
    return time, fuel

def round_up(fuel, ndigits =1):
    result = round(fuel, ndigits)
    if result < fuel:  #In case of round down
        num = type(fuel)
        result += num(10) ** -ndigits
        result = round(result, ndigits)
    return result
    
def output(distance, time, fuel):
    t = str(datetime.timedelta(hours=time)).split(":")
    print("Distance in nautical miles :",distance)
    print("Flight time : {} hour(s) and {} minute(s)".format(t[0],t[1]))
    print("Required fuel : {} gallons".format(fuel))

def main():
    ch = 'y'
    f=0
    print("Aircraft Fuel Calculator")
    while ch == 'y':
        print()
        distance = inputdata()
        print()
        time, fuel = calc(distance)
        roundedUpFuel = round_up(fuel)
        output(distance, time, roundedUpFuel)
        ch = input("Continue? (y/n) : ")
    print("Bye!")
    
main()
