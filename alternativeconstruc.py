class sachin:

    no_of_leaves=12;
    @classmethod
    def print(cls, slevaes):
        cls.no_of_leaves = sleaves;

    def __init__(self,aname,aage,avalue):
        self.name=aname;
        self.age=aage;
        self.value=avalue;
    @classmethod
    def from_dash(cls,string):
        """param=string.split("-");
        return cls(param[0],param[1],param[2]);"""
        return cls(*string.split("-"));
    @staticmethod
    def statci(string,int):
        print("This is an good" +string + " This is an good",int);
    """def __init__(self,aname,aage,afname):
        self.name=aname;
        self.age=aage;
        self.fname=afname;
       """
harry=sachin("sachin",23,34500);
larry=sachin.from_dash("sachin-23-34500");

harry.no_of_leaves=13;
print(harry.no_of_leaves);
print(harry.name);
print(larry.name);
print(larry.age);
print(harry.statci("sachin",23));
print(sachin.statci("sachin",34));