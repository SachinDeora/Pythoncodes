"""class sachin:
    no_of_leaves=8;
    @classmethod
    def change(cls,aname):
        cls.no_of_leaves=aname;

harry=sachin();
harry.no_of_leaves=23;
print(harry.no_of_leaves)
print(harry.__dict__)
"""
class sahil:
    def __init__(self,aname,asalary,arole):
        self.name=aname;
        self.salary=asalary;
        self.role=arole;
    def prints(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}";

class department(sahil):
    def __init__(self,aname,asalary,arole,alanguage):
        self.name=aname;
        self.salary=asalary;
        self.role=arole;
        self.language=alanguage;

    def identity(self):
        return f"The name is {self.name} and the salary is {self.salary} amd the role is {self.role} and the language is {self.language}";




harry=sahil("sachin",12300,"instructor");
sachin=department("sopal",3400,"chomu",["python"]);
sanad=department("sand",34500,"instructors",["python","cpp"]);
print(harry.prints());
print(sachin.prints());
print(sanad.identity())