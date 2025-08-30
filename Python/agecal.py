from datetime import datetime

def calculate_age(birth_date):
    today=datetime.today()
    birth=datetime.strptime(birth_date,"%Y,%m,%d")
    cal=today.year - birth.year - ((today.month,today.day)<(birth.month,birth.day))
    return cal
while True:
    birth_date=input("Enter your birth day : (YYYY,MM,DD) ")
    if(birth_date ==""):
        break
    day=calculate_age(birth_date)
    print(f"Your Age is : {day}")
    
print("Over")