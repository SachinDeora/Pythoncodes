class multiple:
    def __init__(self,aname,aage,aphone):
        self.name=aname;
        self.age=aage;
        self.phone=aphone;
    def prints(self):
        return f"The name is {self.name} and the age is {self.age} and the phone is {self.phone}";

class player:
    def __init__(self,anames,alanguage):
        self.names=anames;
        self.language=alanguage;
    def printss(self):
        return f"The name is {self.names} and the language is {self.language}";

class coolprogrammer(player,multiple):
    languages="c++";
    def printing(self):
       print(self.languages)
    pass;

sachin=coolprogrammer("sachin",234,"instructor");
sahil=coolprogrammer("sachin",["python"])
print(sachin.printss())
print(sachin.printing())
print(sachin.prints())