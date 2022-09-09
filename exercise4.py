print("Please Enter the number");
n=int(input());
print("Please Enter the value");
f=input();
"""n=int(input());
for i in range(n):
    print(i);""";

if f=="True":
    for i in range(n+1):
        for j in range(i):
            print("*",end="");
        print();
print();

if f=="False":
    for i in range(n,0,-1):
        for j in range(0,i,+1):
            print("*",end="");
        print();


