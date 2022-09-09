"""list=[1,2,3,4];
print(list);
list[2]="sachin";
print(list);
for item in list:
    print(item);


list1=[["sachin",1],["sopal",2],["sanad",4]];
for item1,value in list1:
    print(item1,"and is",value);

dict1=dict(list1);
print(dict1);
for item,lol in dict1.items():
    print(item,"and",lol);

for item in dict1:
    print(item);"""

li=["sachin","sopal",1,2,3,6,8];
for item in li:
    if str(item).isnumeric() and item>6:
        print(item);

i=0;
while(i<44):
    print(i);
    i=i+1  
