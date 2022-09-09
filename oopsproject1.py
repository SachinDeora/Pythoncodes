#create a library class
class sachin:
    def __init__(self,aname,avalue):
        self.name=aname;
        self.val=avalue;
        #self.email= f"{self.name} {self.val} @code"
    """def explain(self):
        return f"{self.name} {self.val} @code"
    """
    """@property
    def email(self):
        return f"{self.name} {self.val} @code"""
    @property
    def email(self):
        return f"{self.name} {self.val} @code"
    @email.setter
    def email(self,string):
        name=string.split("@")[0];
        self.name=string.split(".")[0];
        self.val=string.split(".")[1];
harry=sachin("sachin",234);

harry.name="deora";
print(harry.email)
harry.email="deora.sachin"

print(harry.email)

print(id(harry))
print(dir(harry))

#constructor..
#harryLibrary=library(listofbooks,library);

#dictionary.(books-nameofperson)