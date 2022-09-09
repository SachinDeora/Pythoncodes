f=open("data.txt");
print(f.tell());#tell means where is file pointer.
print(f.readline(),end="");

#print(f.tell());
f.seek(10);
print(f.tell());
print(f.readline());
