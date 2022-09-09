class sachin:
    no_leaves=12
    def print(self):
        return f"Name is {self.name}.Salary is {self.section}";

harry=sachin();
vijay=sachin();

harry.name="sabnil";
harry.section=12;

vijay.name=['sachin','sahil'];
vijay.section=12;

print("The name is:- ",harry.name);
print("The section is:- ",harry.section);

print(vijay.print());

class num:
    def __init__(self,aname,asalary,asa):
        self.name=aname;
        self.salary=asalary;
        self.instructor=asa;

sahil=num("sachin",255,"instructor");
print(sahil.name);
print(sahil.salary);