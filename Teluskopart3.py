#constructor
"""class sachin:
    def __init__(self,name,ram):
        self.name=name
        self.ram=ram
    def config(self):
        print(f"The name is:",self.name,"\nThe value is",self.ram)

com1=sachin("ryzen",16)
com1.config()"""
"""class sachin:
    def __init__(self):
        self.name="sachin"
        self.age=14
    def print(self):
        print(f"The name is:-",self.name,"The age is",self.age)
    def  update(self):
        self.age=30
    def compare(self,other):
        if(self.age==other.age):
            return True;
        else:
            return False
s1=sachin();
s2=sachin()
s1.name="sahil khan"
#s2.update()
if s1.compare(s2):
    print("It is same")
else:
    print("it is not same")
s2.update()

print(s1.name)
print(s2.name)
print(s2.age)"""

"""class sopal:
    wheel=4
    def __init__(self):
        self.name="saachin"
        self.age=18
    @classmethod
    def update(cls):
        cls.wheel=18
sp=sopal();
sd=sopal();
sd.update()
print(sp.name,sp.wheel)
print(sd.name,sp.wheel)"""

"""class sopal:
    scholl="sachin"
    def sachins(self):
        self.scholl=34
    @staticmethod
    def sanad():
        print("I am sahil khan")
s1=sopal();
s1.sachins()
sopal.sanad()"""


"""class sachin:
    a=20
    def __init__(self,name,age):
        self.name=name
        self.age=age;
    def print(self):
        print(f"The name is:-",self.name,"The age is:-",self.age)

    @classmethod
    def change(cls,b):
        cls.a=b
    @staticmethod
    def prints():
        print("sachin")

s1=sachin("sachin",18);
s2=sachin("sanad",18)
print(s1)
print(id(s1))
s1.print()
s2.print()
s1.name="ravi"
s1.print()
print(s1.a)
s1.change(23)
print(s2.a);

sachin.prints()
s1.prints()"""

#inner class.
"""class Memory:
    def __init__(self):
        self.name="sachin"
        self.value=1000
        #self.lap=self.Laptop()
    def show(self):
        print(f"The name is",self.name,"The value is :-",self.value);
        # self.lap.show();

    class Laptop:
        def __init__(self):
            self.proc="i5"
            self.ram="8gb"
        def show(self):
            print(f"The processor is:",self.proc,"The ram is:",self.ram)

s1=Memory();
s2=Memory();
s1.show();

s5=s1.lap
s6=s2.lap
print(id(s5))
print(id(s2))
lap=Memory.Laptop();
print(lap.show())
print(type(lap))"""

#inheritance.
"""class sachin:
    def sachin(self):
        print("sachin deora")
    def sachins(self):
        print("sanad khan")

class s2(sachin):
    def sanad(self):
        print("sopal khan")
    def sanads(self):
        print("sachins deora")

class mode(s2):
    def sohal(self):
        print("sopals singh")
    def sohals(self):
        print("sanads khan")
s3=mode();
s3.sanad()
s3.sachins()
s3.sohal();"""

"""class sopal:
    def input(self):
        print("sanad khan")
    def print(self):
        print("sanaks khan")

class sanad:
    def inputs(self):
        print("sanads khans")
    def prints(self):
        print("sanads khan")

class sahil(sopal,sanad):
    pass;

s1=sahil()
s1.prints()"""

"""class sachin:
    def __init__(self):
        print("class a is called")
    def feature(self):
        print("feature-a is called")

class sanad:
    def __init__(self):
        print("CLASS b is called")
    def feature1(self):
        print("sanad khan")

class multiple(sachin,sanad):
    def __init__(self):
        super().__init__();
        print("sanadk khan")
    pass;

s2=multiple();
s2.feature()"""

"""class pycharm:
    def execute(self):
        print("running")
        print("compiling")

class fb:
    def execute(self):
        print("outpuost")
        print("industry")

class sanad:
    def code(self,ide):
        ide.execute()

s1=pycharm()
s2=sanad()
s2.code(s1);"""

#operator overloading.

"""a=10.00
b=20.69
print(a+b)
print(float.__add__(a,b))
print(int.__mul__(a,b))"""

"""class sachin:
    def __init__(self,m1,m2):
        self.m1=m1;
        self.m2=m2;
    def __add__(self, other):
        m1=self.m1+other.m1;
        m2=self.m2+other.m2;
        return m1,m2;

s1=sachin(12,12)
s2=sachin(34,56)
s3=s1+s2
#print(sachin.__add__(s1,s2))
print(s3)"""
"""def sachin(a,b):
    c=a-b;
    d=a+b;
    return c,d;
a,b=sachin(10,20)
print(a)
print(b)"""

"""class sachin:
    def __init__(self,m1,m2):
        self.m1=m1;
        self.m2=m2;

    def __ge__(self, other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2;
        if(s1>s2):
            return True;
        else:
            return False
    def __str__(self):
        #return self.m1,self.m2
        return '{} {}'.format(self.m1,self.m2)
r1=sachin(12,13)
r2=sachin(34,13)
if(r1>=r2):
    print("R1 is greather then r2")
else:
    print("r1 is less than r2")
print(r1.__str__())
print(r2)"""

class sanad:
    """def __init__(self,m1,m2):
        self.m1=m1;
        self.m2=m2;"""

    """def sanad(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c;
        elif a!=None and b!=None:
            s=a+b;
        else:
            s=a;
        return s;"""

    """        def sachin(self,a=None,b=None,c=None):
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!)"""

"""s1=sanad()
print(s1.sanads(1,2,3))"""
#print(s1.sanad(10,29,30))
#Abstract Class.
"""from abc import ABC,abstractmethod
class sachin(ABC):
    @abstractmethod
    def process(self):
        pass;

class sanad(sachin):
    def process(self):
        print("sachin deora")

com1=sanad();
com1.process();"""

#example of abstract class.
"""from abc import ABC,abstractmethod
class sachin(ABC):
    def prints(self):
        pass;

class Sanad(sachin):
    def prints(self):
        print("This is an sachin deora")

class sopal(Sanad):
    def const(self,com):
        print("sahil khan")
        com.prints();

com2=Sanad();
com1=sopal();
com1.const(com2)"""

#iterator.
"""
com1=[1,2,3,4]
it=iter(com1)
print(it.__next__())

print(it.__next__())
print(next(it))"""

"""class ten:
    def __init__(self):
        self.num=1;
    def __iter__(self):
        return self;
    def __next__(self):
        if(self.num<=10):
            val=self.num;
            self.num+=1;
            return val;
        else:
            raise StopIteration
s1=ten();
for i in s1:
    print(i)"""