from Bank import User_Details
class Atm:
    def __init__(self,b):
        self.balance = b
    def deposit(self, amount):
        if amount %100 ==0:
            self.balance += amount
            return f"Deposited: {amount}. New balance: {self.balance}"
        else:
            return "Debosit amount must be in multibles of 100"
    def withdraw(self,amount):
        if amount % 100 ==0:
            if amount <=self.balance:
                self.balance-=amount
                return f"withdrawn : {amount}, available balance is {self.balance}"
            else:
                return "Insufficient balance"
        else:
            return "Withdraw amount must be in multibles of 100"
    def checkBalance(self):
        return f"Available balance is {self.balance}"

# check user details
count =0
while count < 3:
    card_number = input("Enter last 4 digit card number: ")
    pin = int(input("Enter pin: "))
    obj=User_Details(card_number, pin)
    if obj.validate(card_number, pin):
        print("Login successful")
        break
    else:
        print("Invalid credentials, try again.")
        count += 1
while True:
    print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        print(obj.deposit(amount))
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        print(obj.withdraw(amount))
    elif choice == 3:
        print(obj.checkBalance())
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")