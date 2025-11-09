#Lamda function
#lambda argument : expression
""" synatax : lambda argument : expression """
add=lambda a,b : a+b
print(add(1,3))

"""
Key note:
1) lamnda return string

"""
#lamda + map
#map(function , iterator)
fruits=["apple","banana","graps","mango"]

def x(si):
    print(si)
    return si+"hii"
print(list(map(x,fruits)))
"""
Key note:
1) map return map object
2) retrive for list ,tuple
syntax for map:=>   map(function , iterator)
"""
#lamda +filter
#filter function : iterator   => return filter.obj   Based True values
num=[2,5,3,7,6,8,10]
print(list(filter(lambda x : x%2==0 , num)))

num=[2,5,3,7,6,8,10]
def even(x):
    if x%2==0:
        return x
    
print(list(map(even, num))) # o/p [2,None,None ....] map() take to all returned values ,
print(list(map(lambda x:x%2==0, num)))#[True,False,False,...] take Boolean values

from functools import reduce

high=reduce(lambda x,y: x if x>y else y,num)               #53            #5
print(type(high))

a=[3000,500,600,80,3007,5000]
low=reduce(lambda x: x<4000,a)
print(low)

















