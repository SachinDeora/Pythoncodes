def fun1(n):
    #best case.
    if n==0:
        return 1;
    sp=fun1(n-1);
    return n*sp;

#iterative case:-
def iterative(n):
    fact=1;
    for i in range(n):
        fact=fact*(1+i);
    print(fact);




print("Enter the number");
n=int(input());
print(fun1(n));
iterative(5);
