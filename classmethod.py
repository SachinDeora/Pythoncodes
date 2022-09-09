class sachin:
    no_of_leaves=3;
    @classmethod
    def changeleaves(cls,news):
        cls.no_of_leaves=news;

harry=sachin();
sahil=sachin();
harry.changeleaves(34);
sahil.changeleaves(45);
print(harry.no_of_leaves)