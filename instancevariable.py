class instance:
    no_leaves=12;
harry=instance();
larry=instance();

harry.name="saachin";
harry.std=1;
harry.li=["sachin","sahil"];
larry.name="sahil";
larry.subject="maths";

print("No of leaves:-",harry.no_leaves);
print(harry.__dict__);
harry.no_leaves=10;
print(harry.no_leaves);
print(harry.__dict__);
print(larry.__dict__)
print(instance.no_leaves)
instance.no_leaves=13;
print(instance.no_leaves);
print(larry.no_leaves)