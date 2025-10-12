class FindOddEven:
    @staticmethod
    def find(num):
        even=[]
        odd=[]
        for i in num:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        return "Success" ,print(f"Even list: {even} odd list:  {odd}")

n=[1,3,2,5,89,45]
print(FindOddEven.find(n))       
