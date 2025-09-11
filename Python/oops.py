#2pir2
import math
class Teacher:
    def __init__(self,radius):
        self.r=radius
        self.pi=math.pi
class Student(Teacher):
    def __init__(self,radius):
        super().__init__(radius)
    def result(self):
        res=2*self.pi*self.r
        print("result is : " ,res)
obj=Student(16)
obj.result()


#Multiple inheritance
class addition:
    def add(self):
        a = int(input("enter a value"))
        b = int(input("enter b value"))
        c= a+b
        print ("addition is",c)

class subtraction:
    def sub(self):
        a = int(input("enter a value"))
        b = int(input("enter b value"))
        c= a-b
        print ("subtraction is",c)

class multiplication:
    def mul(self):
        a = int(input("enter a value"))
        b = int(input("enter b value"))
        c= a*b
        print ("multiplication is",c)

class division:
    def div(self):
        a = int(input("enter a value"))
        b = int(input("enter b value"))
        c= a/b
        print ("Division is",c)

class final(addition,subtraction,multiplication,division):
    def logic(self):
        self.add()
        self.sub()
        self.mul()
        self.div()
       # pass
# a = final()
# a.add()
# a.sub()
obj2 =final()
obj2.logic()
