list1=["sachin","sahil","sanad"];
"""for i in list1:
    print(i);
print("sachin");

i=0;
while(i<3):
    print("sachin");
    i=i+1;
"""
"""data="sachin";
for i in list1:
    if(i==data):
        continue;
    print(i);
"""
"""a=2;
b=17;
print(a+b);
print(a-b);
print(a*b);
print(a/b);
print(a%b);
print(a**b);
print(b//a);

a+=b;
print("a=",a,"b=",b);
a-=b;
print("a=",a,"b=",b);
a*=b;
print("a=",a,"b=",b);
a/=b;
print("a=",a,"b=",b);
a%=b;
print("a=",a,"b=",b);

a=True;
b=False;
print(a is not b);

a=[1,2,3,4];
if 2 in a:
    print("it is valid");
if 6 not in a:
    print("it is not valid");
"""
"""
def func():
    "This is an doc string"
    print("saachin");
func();

def func1():
    return "sachin";
print(func1());
print("The doc string is:-",func.__doc__);
"""
#Exception handling.
"""
num1=1;
num2="34";
try:
    print("This is an addition")
    num3=num1+int(num2);
    print(num3);

except Exception as e:
    print("Exception is",e);


print("Program continue")
"""
#file Handling.
f=open("data3.txt","r");
#content=f.read();
"""
content1=f.read(15);
print(content1)
print(f.readline())
print(f.tell());
print(f.readline())
f.seek(6);
print(f.readline());
f.seek(0);
print(f.readlines());
#print(f.read());
#print(content);"""
"""print(f.readline())
print(f.tell());
f.seek(0);
print(f.readlines());
"""
"""
f=open("sachin.txt","w");
f.write("sachin deora");
f.close();
f=open("sachin.txt","a")
f.write(" \n sahil khan")
f.close();

f1=open("ds.txt","w");
s=f1.write("sachin dero")
print(s);
f1.close();

f1=open("ds.txt","r+");
content=f1.read();
print(content);

f1.write("This is an amazing Item to introduce yourself");
f1.close();
"""

"""with open("ds.txt","r+") as f:
    content=f.read();
    print(content);
    s=f.write("sachin deor");
    print(s);"""

#inheritance.
"""
class blue:
    def __init__(self):
        print("this is an sachin deora");
    def funct(self):
        print("This is an statement");
class blues:
    def __init__(self):
        super().__init__();
        print("This is an sanad khan")
    def functs(self):
        print("this is an abusive statement");
class multiple(blue,blues):
    def sachi(self):
        print("This is an s elf")

harry=multiple();"""
#Diamond problem.
"""
class a:
    def print(self):
        print("schin");
class b(a):
    def print(self):
        print("sanad");
class c(a):
    def print(self):
        print("sahil");
    def prints(self):
        print("sanad")
class d(b,c):
    def print(self):
        print("d is called")
    pass;

harry=d();
harry.print();
harry.prints();"""


"""class a:
    def __init__(self,aname,avalue):
        self.name=aname;
        self.value=avalue;

    def print(self):
        return f"The name is {self.name} and the value is {self.value}";
    def __add__(self, other):
        return self.value+other.value;
    def __truediv__(self, other):
        return self.value/other.value;
    def __str__(self):
        return self.print();
    def __repr__(self):
        return f"Employee {self.name},{self.value} "
harry=a("sachin",123);
larry=a("sanad",234);
print(harry+larry)
print(harry/larry)
print(repr(harry))"""

# Abstract Method.
from abc import ABCMeta,abstractmethod;
class shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0;

class new(shape):
    def area(self):
        print("This is an sachin deora")
    pass;
harry=new();
print(harry.area())






