"""def func():
    print("substri");
#del func;
func2=func;
del func;
func2();"""

"""def funcret(num):
    if(num==0):
        return print;
    if (num==1):
        return sum ;

a=funcret(0);
print(a);

def execute(func):
    func("this")

execute(print);"""

#Decoraters:It  used in the multiple function in the python;
def dec1(func1):#It returns as a argument in a function.
    def nowexec():
        print("Executing now");
        func1()
        print("executed");
    return nowexec;
@dec1
def harry():
    print("Harray is good boy:");

#harry=dec1(harry);
harry();