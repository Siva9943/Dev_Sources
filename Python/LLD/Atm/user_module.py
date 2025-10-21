from operations import *
import pwinput
print("Welcome to ATM")
print("**************")
print("user login\n")
username=input("Enter the username")
pin=pwinput.pwinput("Enter your pin")
while True:
    print("Enter the operation\n 1)Check balance\n 2)withdrawn\n 3)Deposit \n4)Exit\n")
    user_choice=int(input("Enter your Choice"))
    if user_choice==1:
        pass
    elif user_choice==2:
        pass
    elif user_choice==3:
        pass
    elif user_choice==4:
        break
    else:
        print("Invalid option")
