with open("data2.txt","r") as f:
    print(f.readline());
    f.seek(0);
    print(f.readlines());

f=open("data2.txt","r");
print(f.readline());