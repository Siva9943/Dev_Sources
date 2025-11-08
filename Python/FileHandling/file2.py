import csv

"""
with open("data.csv","r") as csvfile ,open("csvcopy.csv","w") as copy:
    for i in csvfile:
        print(i)
        copy.write(i)


#print age only 

with open("csvcopy.csv", "r") as copy:
    copy1 = copy.readlines()
    for i in copy1[1:]:
        print("*")
        data = i.strip().split(",")
        print(data[1])  # index 1 = age

with open("csvcopy.csv", "r") as copy:
    copy1 = copy.readlines()
    for i in copy1[1:]:  # skip header
        i = i.strip()
        if i:  # skip empty lines
            data = i.split(",")
            print(data[1])
"""
#Dict reader   @import csv

with open("csvcopy.csv", "r") as copy:
    reader=csv.DictReader(copy)
    for row in reader:
        print(row)
        print(row['age'])
