def funtest(n):
    temp=[]
    value=n[1]
    for i in range(len(n)):
        if n[i]!=0:
            temp.insert(0,n[i])
        else:
            temp.append(n[i])
    return temp
    

if "__main__"==__name__:
    p=funtest([2,0,5,3,7,7,0,2,0,4])
    print(p)
