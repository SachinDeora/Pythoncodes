print("Please Enter your number:- ");
n=18;
i=1;
while(i<=9):
    print("Enter the number:-");
    f=int(input());
    if  f>n:
        print("just below the number");
    elif f<n:
        print("just upper the number");
    elif f==n:
        print("you have to won the match");
        print(i,"just took the guess");
        break;

    print("No.of gases left=",i);
    i=i+1;

if(i>=9):
    print("game over");
