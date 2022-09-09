def fun(a,b):
    return a+b;
def fun1():
    print("value of c");

print("call by name is:-",__name__);
if __name__ == '__main__':
    c = fun(2, 3)
    print(c);
    fun1();