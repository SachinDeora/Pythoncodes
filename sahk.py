"""def dec1(func1):#It returns as a argument in a function.
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
"""
def dec1(func1):
    def nowe():
        print("sachi");
        func1();
        print("Excecure");
    return nowe();
@dec1
def harry():
    print("sachin");

#harry=dec1(harry);
harry();