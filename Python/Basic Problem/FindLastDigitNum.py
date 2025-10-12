#method -1
class FindLastNum:
    @staticmethod
    def findLastNum(n):
        num=str(n)
        last=num[len(num)-1]
        
        return int(last)

print(FindLastNum.findLastNum(1230245))
        
#method -2

def findLastN(i):
    num1=str(i)
    return num1[len(num1)-1]

print(findLastN(12389994))
