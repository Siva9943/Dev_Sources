# palindrome checker

def check_palindrome(word):
    revword=word[::-1]
    if (word in revword):
        return "palindrome"
    else:
        return "not a polindrome"

n=input("Enter the string input : ")
print(check_palindrome(n))

# Gussing game
import math
def gussing_Game():
    randomNum=math.random(100)*100
    print(randomNum)
gussing_Game()