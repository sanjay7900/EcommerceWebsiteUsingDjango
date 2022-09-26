
from user.models import Product_info, Userlogin

class logincheck():
    def checkuser(self,user,passwd):
        print(user,passwd)
        self.temp=Userlogin.objects.filter(Email=user,password=passwd).values()
        #print(self.temp)
        return self.temp
class sign_up():
    confirm=False

    def check_not_allready(self,user,passwd):
        self.getuser=Userlogin.objects.filter(Email=user,password=passwd).values()
        
        if not self.getuser:
           self.confirm=True
           
        else:
            self.confirm=False    
        return self.confirm
        
    
        
