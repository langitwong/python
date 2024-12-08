#
#
#
exception = "Invalid, please try again!"

# ATM functions, deposit, withdraw, and show balance.

def showBalance(balance):
	print(f'Your balance is {balance}')
	print(" ")

def deposit(amount):
	return amount

def withdraw(amount, balance):
	if amount > balance:
		print(f"{exception}")
		return 0
	elif amount < 0:
		print(f"{exception}")
		return 0
	else:
		return amount

helloWorld = True # Condition for while loop, we can manipulate anytime.
balance = 0 # Init balance is 0

while helloWorld:
	print("+" * 20)
	print("+ ATM" + " " * 14 + "+")
	print("+" * 20)
	print("+ 1. Show balance" + " " * 2 + "+")
	print("+ 2. Deposit"  + " " * 7 + "+")
	print("+ 3. Withdraw"  + " " * 6 + "+")
	print("+"  + " " * 18 + "+")
	print("+ 4. EXIT"  + " " * 10 + "+")
	print("+" * 20)

	choice = int(input("$ "))
	if choice == 1:
		showBalance(balance)
	elif choice == 2:
		balance += deposit(int(input("$ Amount: ")))
		print(" ")
	elif choice == 3:
		balance -= withdraw(int(input("$ Amount: ")), balance)
		print(" ")
	elif choice == 4:
		helloWorld = False
	else:
		print(f'{exception}')

	

 
