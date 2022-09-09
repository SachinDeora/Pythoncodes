class a:
    def __init__(self):
        print("sachin is called");
    def function1(self):
        print("function 1 is called");
class b:
    def __init__(self):
        print("sahil khan")
    def function1(self):
        print("function-1 is calling")


"""class b(a):
    def __init__(self):
        super().__init__()
        print("sahil khan")"""

class c(b,a):
    def __init__(self):
        super().__init__();
        print("sopal khan")
b=c();
b.function1();