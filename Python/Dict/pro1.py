student={
    "Alice":40,
    "siva":99,
    "banu":88,
    "aji":94,
    }
 # grater than 80 students

result={}

for key,value in student.items():
    if value>80:
        result[key]=value
print(result)

h=[k for k,v in student.items() if v>80]
print(h)
