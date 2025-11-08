class UserData:
    def __init__(self,**data):
        self.UserInfo=data
        self.OverallData={}
    def signupUser(self):
        self.OverallData+=self.UserInfo
        return "Successfully Saved!......"

class UserOperation(UserData):
    def __init__(self,in_Username,in_Password):
        self.in_Username=in_Username
        self.in_Password=in_Password
    def checkUser(self):
        super().UserData({"name":"siva","password":943268})
        pass
data={"name":"siva","password":9432}
obj=UserOperation("siva",93433)
obj.signupUser()
        
