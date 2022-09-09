"""class moti:
    no_of_leaves=12;

    def __init__(self,aname,aval,aage):
        self.name=aname;#name is an instance member variable.
        self.salary=aval;
        self.age=aage;


    @classmethod
    def change(cls,nleaves):
        cls.no_of_leaves=nleaves;
    def sachin(self):
        return f"The name is:{self.name} and the salary is{self.age} and the age is {self.salary}";
harry=moti("sachin",12300,34);
sanad=moti("sahail",1239,23);
print(harry.sachin())
harry.change(13);
print(harry.no_of_leaves)
print(sanad.no_of_leaves)

print(sanad.__dict__)
print(harry.__dict__)"""
#print(sanad)
#sanad=moti();
#harry.sachin();
"""harry.name="sachin";
sanad.classs="12th";
print(harry)
print(harry.name);
#print(sanad.name);
print(sanad.classs)
print(harry.__dict__)
print(sanad.__dict__)
print(harry.no_of_leaves)
print(harry.__dict__)
harry.no_of_leaves=13;
print(harry.no_of_leaves)
print(sanad.no_of_leaves)
moti.no_of_leaves=34;
print(moti.no_of_leaves)
print(moti.__dict__)
print(harry.__dict__)
print(sanad.__dict__)"""

""""class sachin:

    def __init__(self):
        print("sachin deora");
    def prints(self):
        print("This is an view")

class view:
    def __init__(self):
        print("sanad khan")
    def printss(self):
        print("This is an sahil")

class multiple(view,sachin):
    pass;

sachins=multiple();"""

"""class variagle:
    __protect=12;

harry=variagle();
print(harry._variagle__protect)

print(5+6);
print("sachin"+"deora")"""

"""class harry:
    def __init__(self):
        print("sachin deorA");

class sachin(harry):
    def __init__(self):
        print("sanad khan");
        super().__init__();

abhishek=sachin();"""
"""class sachin:
    def __init__(self,aname,asal,aval):
        self.name=aname;
        self.sal=asal;
        self.val=aval;


    def print(self):
        return f"The name is {self.name} and the salary is {self.sal} and the value is {self.val}";

    def __repr__(self):
        return f"employee is ({self.name},{self.sal},{self.val})"

    def __str__(self):
        return self.print();
harry=sachin("sachin",234,"12");
sanad=sachin("sopal",345,"21");"""
"""print(harry+sanad);
print(harry*sanad);
print(harry/sanad)"""
"""print(id(harry))
print(id(sanad))"""
"""print(type(harry))
print(dir(harry))"""
from abc import ABCMeta,abstractmethod;
class sachin(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        return 0;

class sopal(sachin):

    def print(self):
        print("sachin deora")
    def sanad(self):
        print("sanachin");

harry=sopal();
harry.sanad();



