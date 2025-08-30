def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("please select your operation- 1.ADD\n , 2.SUB\n , 3.MULTIPLE \n , 4.DIVIDE\n");
# input section
select =int(input("Select into 1,2,3,4\t"))
number1=int(input("Enter the num1"));
number2=int(input("Enter the num2"));
if select ==1:
    print("result:\t",add(number1,number2))
elif select ==2:
    print("result:\t",subtract(number1,number2))
elif select ==3:
    print("result:\t",multiply(number1,number2))
elif select ==4:
    print("result:\t",divide(number1,number2))
                    
          

