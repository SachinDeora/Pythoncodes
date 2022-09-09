class a:
    def met(self):
        print("This is an calass");
class b(a):
    def met(self):
        print("This is an a1 class");
class c(a):
    def met(self):
        print("This is an used cases");
    def mets(self):
        print("sanad khan")
class d(b,c):
    def met(self):
        print("This is an used cases of d")
    pass;


harry=d();
harry.met();
harry.mets();