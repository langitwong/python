#
#
#
def addMoney(money):
	return money
	
helloWorld = True
wallet = 0

while helloWorld:
	print("1. Show balance")
	print("2. Deposit")
	choice = int(input("$ "))

	if choice == 1:
		print(f'{wallet}')
	elif choice == 2:
		money = int(input("$ Amount: "))
		wallet += addMoney(money)
	else:
		helloWorld = False


