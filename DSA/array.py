my_array = [7, 12, 9, 4, 2,1,11]
first=my_array[0]
#secound lowest
sec=[]
for i in my_array:
    if first>i:
            first=i
            sec.insert(0,i)
print(sec[1])
