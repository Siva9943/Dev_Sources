def loveCalculator(name1,name2):
    count_true=0
    count_love=0
    same_letter=0
    for i in name1:
        if i.lower()in "true":
            count_true+=1
        elif i.lower() in "love":
            count_love+=1
    for i in name2:
        if i.lower()in "true":
            count_true+=1
        elif i.lower() in "love":
            count_love+=1
    
    return int(str(count_true)+str(count_love))+same_letter
name1=input("Enter your first name") 
name2=input("Enter your Secound Name")
print(loveCalculator(name1,name2))


