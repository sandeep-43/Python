#import sys
#x = int(input ('enter a range'))
for x in list(range (1,4)):#giving a user 3 chances to enter a number
	print (list(range (1,4)))
	num = int(input ('enter a number'))
	while num <= 10:
		print ('the number ', num,' is  good')
		num+=1
	else:
		print ('the number ', num,' is not good')  
   
else:
	print ('sorry! No more chance')
