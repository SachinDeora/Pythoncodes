class a:
    def met(self):
        print("This is an calass");
class b(a):
    def met(self):
        print("This is an a1 class");
class c(a):
    def met(self):
        print("This is an used cases");
class d(b,c):
    pass;

harry=d();
harry.met();