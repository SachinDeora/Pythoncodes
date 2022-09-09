"""from numpy import *
ar=array([
    [1,2,3,4,5,3],[1,3,4,2,3,4]
])
print(id(ar))
print(ar)
print(ar.dtype)
print(ar.ndim)
print(ar.shape)
print(ar.size)

ar2=ar.flatten();
print(ar2)
ar3=ar.flatten()
ar4=ar2.reshape(2,2,3)
print(ar4)


ar5=array([
            [1,2,3,4],[3,4,5,6]
])

print(ar5)
ar=matrix(ar5)
print(diagonal(ar))
print(ar.sum())
print(ar.max())
print(ar.min())
ar6=array([
            [1,2,3,4],[3,4,5,6]
])
ars=ar*ar5
print(ars)"""
"""
def sachin(name,**age):
    print(name);
    for i,j in age.items():
        print(i,j)

sachin('sachn',age=11,roll=12,nam=34)"""

"""a=10
def person():
    a=11
    print(a)#Local variable.
    x=globals()['a']
    print(x)
    globals()['a']=20


person()
print(a)"""

"""fact=1;
print("Enter the number:-");
a=int(input());
for i in range(1,a+1):
     fact=fact*i;
print("the factorial number is:-",fact)"""

"""def fact(x):
    f=1;
    for i in range(1,x+1):
        f=f*i;
    print(f)
fact(5)"""
"""import sys;
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())"""

"""def fact(n):
    if(n==0):
        return 1;
    return n*fact(n-1)

c=fact(5)
print(c)

f=lambda a:a*a;
e=lambda a,b:a+b
b=f(10)
print(b)
c=e(20,10)
print(c)"""

"""def div(a,b):
    print(a/b)

def sub_div(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner;

div1=sub_div(div)
div1(2,4)"""

"""def fact(n):
    if(n==0):
        return 1;
    return n*fact(n-1)
c=fact(5)
print(c)
a=lambda a,b:a*b;
b=a(2,3)
print(b)"""

#decorators.
"""def div(a,b):
    print(a/b)

def sub_div(func):

    def inner(a,b):
        if(a<b):
            a,b=b,a;
            return func(a,b)
    return inner;

div1=sub_div(div)
div1(2,4)"""
"""import sd as s;
from sd import *;
a=10
b=20
c=add(a,b);
print(c);"""

if(__name__=="__main__"):
    print("sachin deora" + __name__)
    print("sachi")