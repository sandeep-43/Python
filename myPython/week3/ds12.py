num = int(input('Please input a number:'))

if num > 0:
    # Nested if
    if num > 30:
        print ('You input a number greater than 30')
    # For `0 < num <= 30`
    else:
        print ('You input a positive number which is not greater than 30')
else:
    # For `num <= 0`
    print ('You input number which is not greater than 0')