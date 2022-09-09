from array import *;
#import math as m
"""from math import sqrt,pow;
a=5;
b=2;
c=a//b;
d=a**b;
print(c);
print(d)
f=a%b;
print(f);
a="sachin"
print(a);
print("navin's laptop")
print("navin 'laptop'")
print('navin\'s "laptop"')
print("naving"+"navin")
print(10*"navin",end="\n")
print('c:\docs\\navin');

#variables in python.
x=2;
x=x+3;
print(x);
x=6;
print(x);
print(type(x));
print(x+19);
print(x);
nums=[1,2,3,4];
print(nums);
print(nums[0])
print(nums[3])
print(nums[2:]);
print(nums[:3])

names=['navin','kiarna','jjo'];
print(names)
val=[1,2,3,'sachin','deora',5];
print(val)
print(val[3:])
mil=[names,val];
print(mil);
print(names.append(4))
print(names)
names.clear()
print(names)
names.insert(2,34);
print(names)
print(val)
print(val.insert(2,34))
print(val)
val.remove(34);
print(val)
#it means how to delete the particular index.
val.pop(3);
print(val)
val.pop();
print(val)
#it means how to delete the multiple value in list by using index.
del val[2:4]
print(val)
#It means how to add multiple value in list.
val.extend([23,23,12]);
print(val)
print(min(val))
print(max(val))
print(sum(val))
nums.sort()
print(nums)
nums.reverse()
print(nums)

#Tupple.
tup=(1,2,3,4,34,3);
print(tup)
print(tup[1])
#tup[1]=12;
print(tup)
tup.count(3)
print(tup.count(3))
print(tup.index(2))

#set:-collection of unique elements.
#it will work only integer values.
s={122,34,53,21,5};
print(s);
s={2,3,4,5,2,4};
print(s);
print(s.add(12));
print(s);

#More on variables.
num=5;
print(id(num))
name="sachin"
print(id(name))
se=12;
sf=se;
print(id(se));
print(id(sf))
print(id(12))
se=3;
print(id(se))
print(id(sf))
print(sf)
pi=3.14;
print(pi)
#Data types in python
i=10;
print(type(i))
num=2+3j
print(type(num))
n=10.5;
m=int(n);
print(m)
k=float(m);
print(k)
y=complex(m,k)
print(y)
a=True;
print(type(a))
b=int(True)
print(b)
a=range(0,20);
b=list(range(10));
print(b)
c=list(range(2,10,2))
print(c);
#dictionary.
nd={1:"sachin","sachin":23};
print(nd["sachin"])
print(nd.keys())
print(nd.values())
print(nd.items())
print(nd.get("sachin"))
f=list(nd.items());
print(f)
print(type(f))

#operators in python.
a,b=5,6;#assingment the value in one line.
print(a);
print(b);
#urnary operator.
n=7
print(n);
n=-n;
print(n)
a=2;
b=3;
a=2;
b=3;
print(a>b and a<b)
print(a<b or a>b)
print(not a)
li=[1,2,3,4];
b=21 in li;
print(b)
a=12;
b=12;
c=a
print(a is b)
print(a is not c)
#Binary conversion.
a=bin(25);
print(a);
a=0b0101
print(a)
a=oct(23)
print(a)
a=hex(10)
print(a)
x=bin(65)
print(x)
#bitwise
a=~-123
print(a)
a=15;
b=17
print(a&b)
print(6|7)
print(12^14)
print(6<<2)
print(6>>2)

a,b=10,20;
print(a)
print(b)
#swap two variables.
a,b=b,a;
print(a)
print(b)
#mathmodule
x=math.sqrt(25)
print(x)
print(math.floor(2.6))
print(math.ceil(2.4))
print(math.pow(2,3))
print(math.pi)
print(math.e)

print(sqrt(12))
#userinput in python.
print("enter  the value of a")
a=input();
b=input("Enter second number")
c=int(a)+int(b);
print(c);
print(type(a))
#print a single character by using input.
a=input("Enter a value")[0]
#print(a[0]) one way to get single character.
print(a)
#evaluate the number.
b=eval(input("enter the expression"))
print(b)"""
#conditional statement.
"""if False:
    print("sachin deora")

a=int(input("Enter the value of a"));
r=a%2;
if r==0:
    print("Even");
    if(a>4):
        print("value is greater then 4")
    else:
        print("value is less than 4");
else:
    print("odd number")
"""

#break statement.
"""av=10;
a=int(input("How many candies you are paying:-"));
i=1
while(i<=a):
    if(i>av):
        print("out of stock")
        break;

    print("candy");
    i+=1;
print("bye")"""

#Continue Statement.
"""for i in range(1,101):
    if(i%3==0 and i%5==0):
        continue
    print(i)"""
#pass statement.
"""for i in range(1,101):
    if(i%2!=0):
        pass;
    else:
        print("print only even number",i)"""

#printing pattern.
"""for i in range(4):
    for j in range(4):
        print("*",end=" ");
    print()"""

"""for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()
print()
for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()"""

#for else.

"""for i in [1,2,51,23,34,301]:
    if(i%5==0):
        print(i);
        break;
else:
    print("Not found")"""

"""val=array('i',[1,2,3,4,-2,-3])
print(val[0])
vals=array('I',[2,3,4,3])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
vals.reverse();
print(vals)
for i in range(len(vals)):
    print(vals[i])
for i in vals:
    print(i)

ve=array('u',['c','d','e','f'])
print(ve)

#copying the value from one array to another array.
vs=array(vals.typecode,(a*a for a in vals))
for i in vs:
    print(i)

i=0;
while(i<len(vs)):
    print(vs[i])
    i+=1;"""

"""arr=array('i',[])
print("Enter the length of an array")
n=int(input());

for i in range(n):
    x=int(input("Enter next value in array:-"))
    arr.append(x);

for s in arr:
    print(s)"""

#searching the value in array.
arr=array('i',[])
print("Enter the length of an array:-");
n=int(input())

for i in range(n):
    x=int(input("Enter the next value:-"))
    arr.append(x);

print("Enter the searching value in a arrayL:-");
search=int(input());
for i in range(len(arr)):
    if(arr[i]==search):
        print("The index value is:-",i);
        break;
k=0;
for i in arr:
    if(i==search):
        print(k)
        break;
    k+=1;
#To find the value by using function.
print(arr.index(search))