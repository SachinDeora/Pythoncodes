class a:
    def features(self):
        print("sachin deora");
    def feautre1(self):
        print("sahil khan");

class b(a):
    def feautre2(self):
        print("kyuber");
    def feature3(self):
        print("price");
class c(b):#multi level inheritance
    def features3(self):
        print("nish");
    def feaurte(self):
        print("harshit");

class d(b,c):#multiple inheritance.
    pass;
harry=b();
sanad=c();
sopal=d();
harry.features()
