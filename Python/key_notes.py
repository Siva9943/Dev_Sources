def data(**d):
    print(type(d))
    print(d["name"])
#data(name="siva",age=22)

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
#print(fact(0))

n=[2,4,5,6,7]
x=lambda a:a+1
for i in n:
    print(x(i))

 
