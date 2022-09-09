class sachin:
    no_of_leaves=12;#public modifiers.
    _sac=23;#protected variable.
    __private="sachin"#private variable.
    def __init__(self,aname,aage,acity):
        self.name=aname;
        self.age=aage;
        self.city=acity;
    def function(self):
        return f"The name is {self.name} and the age is {self.age} and the city is {self.city}";

harry=sachin("sachin",21,"sikar");
print(harry.no_of_leaves);
print(harry._sac);
print(harry._sachin__private);