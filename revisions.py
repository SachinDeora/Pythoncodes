def fun(normal,*args):
    for i in args:
        print("value of i is:=",i);
    print(normal);
def fun1(*args,**kargs):
    for s in args:
        print("value of arguments is:-",s);
    for key,value in  kargs.items():
        print(f"The value of key is {key} and the value is {value} ");
li=["sachin","deora","sahil"];
dict={"schin":"deora","art":"gallery","sahil":"sharma"};
normal="sahid";
fun(normal,*li);
fun1(*li,**dict);