from array  import *
from numpy import *
"""var=array('i',[1,2,3,4,-1,-2])
for i in var:
    print(i)
print(var.typecode)
print(var.buffer_info())
var.reverse()
print(var)
new=array(var.typecode,(n for n in var))
for i in new:
    print(i)

arr=array('i',[])
print("Enter the length of an array:-");
n=int(input())
for i in range(n):
    print("Enter the next value in array:-")
    x=int(input())
    arr.append(x);

for i in arr:
    print(arr)
    break;

for i in range(len(arr)):
    print(arr[i],end=" ")"""

""""var=array('i',[])
print("Enter the length of an array:- ")
n=int(input())
for i in range(n):
    print("Enter the next value:-")
    x=int(input())
    var.append(x)

search=int(input("Enter the data searching in an array:-"))
for i in range(len(var)):
    if(var[i]==search):
        print("the index value is:-",i)
        break;
        
print(var.index(search))"""

"""for i in [1,2,3,4,5,10]:
    if(i%5==0):
        print(i);
        break;
else:
    print("not found")

for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()"""

"""var=array([1,2,3,4,3.5],int)
print(var)
print(var.dtype)
var=array([1,2,3,43],float)
print(var)
print(var.dtype)
vars=linspace(0,15)
print(vars)
vars=logspace(0,15,5)
print(vars)
vars=arange(0,15,6)
print(vars)
var=zeros(5,int)
print(var)
var=ones(5,float)
print(var)"""
"""n=matrix('1 2 3 ; 1 2 4 ; 1 2 3')
m=matrix('1 2 3 ; 1 2 3 ; 1 2 5')
s=n*m;
print(s)"""
#function in python
"""def add_sub(x,y):
    c=x+y;
    d=x-y;
    return c,d;


result,result1=add_sub(2,3)
print("The value of first is",result,"The value of seconed is:-",result1)

def update(a):

    print(id(a))
    a[0]=1
    print(id(a))
    print(a)
a=[3,4,5];
print(id(a))
update(a)
print(a)
#Types of Actual Arguments.
#1.position or keyword
def position(name,age):
    print(name);
    print(age-5);
position(age=12,name='sachin')

#2.Default.
def position(name,age=12):
    print(name)
    print(age)
position('sachin')

#3.variable length.
def sum(a,*b):
    print(a)
    print(b)
    c=a;
    for i in b:
        c=c+i;
    print(c)

sum(1,2,3,4)

#Keyword variable length argument.
def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
     print("The value of key is:-",i,"The value is:-",j)

person('sachin',age=18,work='jaipur',workplace='mumbai')"""

#Global and Globals function.
"""a=10
def person():
    global a;
    a=5;
    print("local varaible:-",a)
    a=20
person();
print("global variable:-",a)"""

"""a=13
print(id(a))
def person():
    a=12;
    x=globals()['a']
    print("Local variable:-",a)
    print(id(x))
    #x=20
    #print(x)
    #print(id(x))
    globals()['a']=20
    print(x)
    print(id(x))
person();
print("global variable:-",a)

"""

#assignment pass a list as a function return as odd or even number.


"""def count(lst):
    even=0
    odd=0
    for i in lst:


        if(i%2==0):
            even+=1
        else:
            odd+=1;
    return even,odd
lst = [2, 3, 4, 5, 6, 4, 56];
even,odd=count(lst)
print("The even number is:-",even)
print("the odd number is:-",odd)
print("Even is:{} and odd is:{}".format(even,odd))"""

#Revision.
"""ar=array([1,2,3,4,5])
ar2=ar.view()
ar[1]=5
print(ar)
print(ar2)
ars=array([2,3,4,5])
ar1=ars.copy();
ars[3]=6
print(ars)
print(ar1)"""

ars=([
    [1,2,3],[2,3,4]
])

print(ars)











