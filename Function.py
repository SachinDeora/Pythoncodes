"""a=int(input());
b=int(input());
c=sum((a,b));#predefined function.
print(c);"""

def function1(a,b):
    print(a+b);

a=int(input());
b=int(input());
function1(a,b);
print(function1(a,b));

def function1(a,b):
    avg=(a+b)/2;
    return avg;

c=function1(2,2);
print(c);
print(type(c));

def fun1(a,b):
    """This is an average number printing"""
    avg=(a+b)/2;
    return avg;

print(fun1.__doc__);