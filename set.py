s=set();
print(type(s));
sl=set([1,2,3,4]);
print(sl);
print(type(sl));
l2=[1,2,3];
sl=set(l2);
print(sl);
s.add(1);
print(s);
s.add(2);
print(s);
s.add(1);
print(s);
s.remove(2);
print(s);
s1=s.intersection({1,2,3});
print(s1);