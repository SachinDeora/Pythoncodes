dic={"sachin":"deora","sahad":"tuglak"};
print(dic["sachin"]);
print(type(dic));
ds={"sachin":"deora","sahad":"tuglak","shubham":{"b":"lahasan","e":"snacks","d":"hm"}};
print(ds);
ds[420]="sachin";
#append the dictionary or change the value of name to key.
print(ds);
#delete the 420 in dicitionary;
del ds[420];
print(ds);
d3=ds.copy();
#del d3["sachin"];
print(ds);
print(ds.get("sachin"));
ds.update({"tm":"tsd"});#it means add new value.
print(ds);
print(ds.keys());
print(ds.items());#key and value pairs.

