#numbers=["2","56","74"];

"""for i in range(len(numbers)):
    numbers[i]=int(numbers[i]);
"""
"""numbers=list(map(int,numbers));
#print(num);
numbers[2]=numbers[2]+1;
#print(numbers[2]);
print(numbers[2]);

def sq(a):
    return a*a;
num=[2,3,4,5,6,2,24,5];
#num=list(map(sq,num));
square=list(map(lambda x:x*x,num))
print(square);
"""

"""def square(a):
    return a*a;
def cube(a):
    return a*a*a;

num=[2,3,4,5,5,6,7];
func=[square,cube];
for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val);

#filter function.
list1=[1,2,3,4,5,7];
def is_greater(num):
    return num>5;

gr_than_5=list(filter(is_greater,list1));
print(gr_than_5);
"""

list1=[2,3,4,5,6];
def greater(num):
    return num>5;

ga=list(filter(greater,list1));
print(ga);
def add(x,y):
    return x+y;
from functools import reduce;
list2=[1,2,3,4];
#num=reduce(add,list2);
num=reduce(lambda x,y:x+y,list2);
print(num);

num=0
