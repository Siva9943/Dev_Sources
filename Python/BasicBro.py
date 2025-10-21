k=0
l='30hskjksf'
def basic():
    global o
    o=2323
    print(list(l))
    u=list(l)
    result=[]
    for i in range(len(u)-1):
        if u[i]in "1234567890":
            result+=u[i]
    a=str(result)
    return a
p=basic()
print(p)




