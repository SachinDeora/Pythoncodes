"""def fun(*args):
    print(type(args));
    for i in args:
        print(i);"""
    #print(args[0]);
#2.If you have to pass any normal variable.
def fs(normal,*argw):
    print(argw[0]);
    print(normal);

def fs(*argw,**kwargs):
    for i in argw:
        print(i);
    print("\n I would like to introduce new things.")
    for key,value in kwargs.items():
        print(f"The {key} is {value}");
l=["sachin","deora","sahil"];
ns="sachn deora"
d={"sachin":"ceo","shruti":"cofounder","samad":"sahil"};
#fun(*l);
fs(*l,**d);