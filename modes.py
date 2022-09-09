#Return the Text file data.
"""f=open("data.txt");
content=f.read();
print(content);

#Return the Binary file data.
f=open("data.txt","rb");
content=f.read();
print(content);

f=open("data.txt","r");
content=f.read(3);#Read three content.
print("1",content);

content=f.read(3);#Read three content.
print("2",content);"""
f=open("data.txt","r");
#c=f.read();
#Print the file in the line by line.
"""for i  in c:
    print(i);"""
"""for i in f:
    print(i,end="");"""#it takes by default print one new line to stop the new line and space used end.
"""ReadLine
print(f.readline(),end="");
print(f.readline());"""
"""Readlines:-It means store the data in a single list.
print(f.readlines());"""
f.close();