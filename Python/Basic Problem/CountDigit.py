class CountDigi:
    def countDigit(self,num):
        count=0
        n=str(num)
        for i in range(len(n)-1):
            if n[i]:
                count+=1
        return count+1
obj=CountDigi()
print(obj.countDigit(5678899984344459845))
