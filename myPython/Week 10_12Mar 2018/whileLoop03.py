limit = 1000; interest = 0.1
balance = float (input('enter a balance: '))
while balance < limit:
	#print ('the balance is now: ', balance)
	balance =balance + balance * interest
	print ('the balance is now: ', balance)
else: print ('balance is greater than limit')

