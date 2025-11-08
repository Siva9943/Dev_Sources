#fibno series
#loop
"""
def fibno(n):
    n1=1
    n2=0
    for i in range(n):
        if i==0:
            print(0)
        new=n1+n2
        print(new)
        n1=n2
        n2=new
num=int(input("Enter the n th number"))
fibno(num)

# Recursion
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)
"""

def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(1))

