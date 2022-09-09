l=20 #Global Variable.
def fun(n):
    l=5#local variable.
    print(l);
fun(20);

print(l);
#Global keyword:-if i have to change the global variable value in the function.
f=30
def fun1(n):
    global f;
    f=f+20;
    print(f);
fun1(20);

#some question:-
x=23;
def se():
    x=34;
    def sm():
        global x;
        x=24;
    print("before the  calling:-",x);
    sm();
    print("after the calling:-",x);
se();
print(x);