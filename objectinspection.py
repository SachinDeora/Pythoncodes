class sachin:
    def __init__(self,name,value):
        self.name=name;
        self.value=value;

    def explain(self):
        return f"{self.name} and {self.value}";

a=sachin("sachin",123);
print(type(a));
print(id(a))
print(dir(a))