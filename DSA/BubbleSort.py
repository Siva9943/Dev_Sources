#Bubble sort
n=[54,83,87,9,2,3,5,21,90]
for i in range(len(n)-1):
    for j in range(len(n)-i-1):  
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)

#Note         
"""
1)swaps values if the first value is higher than the next value
2)this inner loop must run (n-i-1) times.
