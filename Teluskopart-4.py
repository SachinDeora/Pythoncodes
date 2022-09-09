#Exception Handling.
"""a=2
b=0
try:
    print("registration opened")
    print(a/b)
    print("registration closed")
except ZeroDivisionError as e:
    print(e)
finally:
    print("registration closed")"""

#File Handling.
#1.files.
"""f1=open("ds.txt","r")
print(f1)
print(f1.readline())
print(f1.read())"""

"""f1=open("ds.txt","a")
f1.write("I am not perform an individual task and i am doing perform some taks")"""
"""f1=open("ds.txt")

f1=open("ds.txt","r")
f=open("data.txt","w")

for i in f1:
    f.write(i)"""
"""f1=open("ds.txt")
print(f1.readline())
print(f1.tell())
#It means to reset the filepointer
f1.seek(184)
print(f1.readline())"""

#Thread
from threading import *;
from time import sleep;
class Sachin(Thread):
    def run(self):
        for i in range(5):
            print("Thread 1:-",i);
            sleep(1)

class Sanad(Thread):
    def run(self):
        for i in range(5):
            print("Thread 2:-",i)
            sleep(1)

s1=Sachin();
s2=Sanad();
s1.start()
sleep(0.2)
s2.start();
s1.join()
s1.join()
#sleep(1)
#print("Bye")
print("Bye")