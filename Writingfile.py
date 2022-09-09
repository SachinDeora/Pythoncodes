#Write the data in the file.
"""f=open("data.txt","w");
f.write("sachin deora");
f.close();
s=open("data1.txt","w");
s.write("This is an sahil khan");

s.close();"""
"""
f=open("data.txt","a");
a=f.write("sachin deora\n");#it means only you are writing the charcter in f.write() to return only this value.
print(a);
"""
#Handle Read and write data in the file.
f=open("data.txt","r+");
content=f.read();
print(content);
f.write("sopal singh");
f.close();
print(content);