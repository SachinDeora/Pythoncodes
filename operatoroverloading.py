class a:
    def __init__(self,aname,asalary,arole):
        self.name=aname;
        self.salary=asalary;
        self.role=arole;

    def prints(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}";

    def __add__(self, other):#dendor add method.
        return self.salary+other.salary;

    def __truediv__(self, other):  # dendor add method.
        return self.salary / other.salary;
    """def __repr__(self):
        return self.prints();"""
    def __repr__(self):
        return f"Employe('{self.name}',{self.salary},'{self.role}')";
    def __str__(self):
        return self.prints()

harry=a("sachin",123,"instructoer");


rohan=a("sanad",334,"computer");
print(harry/rohan)
print(harry);
print(repr(harry))