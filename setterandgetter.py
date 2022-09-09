"""def sachi():
    print('sachin');

sach=sachi;
sach();
"""
#decoraters
"""
def dec(func1):
    def now():
        print("executed");
        func1()
        print("executed");
    return now;
@dec
def sachin():
    print("new");

sachin();
sachin=dec(sachin)
"""
#sachin();

class employee:
    def __init__(self,fname,lname):
        self.name=fname;
        self.last=lname;
        #self.email=f"{fname} {lname} @codewithharry"
    def explain(self):
        return f"This employee is {self.name} and the last name is {self.last}"
    @property#to just pass as argument in email.it just used as change the fname and lname
    def email(self):
        if(self.name==None or self.last==None):
            print("please set the email in the setter")
        return f"{self.name} {self.last} @sachindeora"

    @email.setter
    def email(self,string):
        print("setting now");
        name=string.split("@")[0];
        self.name=string.split(".")[0];
        self.last=string.split(".")[0];
    @email.deleter
    def email(self):
        self.name=None;
        self.last=None;

harry=employee("sachin","deora");
larry=employee("sanad","khan");
#print(harry.email())
harry.name="shruti"
#print(harry.email())
print(harry.__dict__)
print(larry.__dict__)
#print(harry.explain());
#print(harry.email)
#The email just pass as an argument.
print(harry.email);
harry.name="shruti";
print(harry.email)
#setter atrribute:-It means i have to set the email attribute then used setter atrribute
#harry.email="this.that@sachindeora" This is an error.
harry.email="this.that";
print(harry.email)
#if i want to delete the email then used email delter
del harry.email;
harry.email;