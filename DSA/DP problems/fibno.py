#memorization technique
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
n=int(input("Enter the number : "))
print(fib(n))
#Tobulation technique (buttom to up)

def fibno(n):
    result=[0,1]
    for i in range(2,n+1):
        result.append(result[i-1]+result[i-2])
    return result[n]
n=int(input("Enter the number : "))
print(fibno(n))


