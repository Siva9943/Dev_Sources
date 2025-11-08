n=999444444498
num=list(str(n))
#num="sivaprakash"
count={}
for i in num:
    count[i]=count.get(i,0)+1
print(count)

