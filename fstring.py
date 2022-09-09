import math;
a="sachin";
a1=23;
c="this is %s %s"%(a,a1)#Not Readable.
d="this is {1} {0}";#Not Readable
b=d.format(a,a1);
z=f"this is {a} {a1} {math.cos(45)}";#fstring.
print(z);
print(c);
print(b);