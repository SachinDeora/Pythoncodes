class a:
    var="sachin";
    def __init__(self):
        self.var=23;
        self.special="sanad";
class b(a):
    var="sanad"
    def __init__(self):

        self.var="sachin";
        super().__init__()#to override the var variable.
    pass;
harry=b();
print(harry.var);
print(harry.special)