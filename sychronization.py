from threading import *;

class Table: #shared resoruces.
    def print(self,number):
        for i in range(1,11):
            print(number,'x',i,'=',number*i);


class MyThread(Thread):
    def __init__(self,tableobj,number):
        Thread.__init__(self)#called as a super class constructor.
        self.tableobj=tableobj;
        self.number=number;

    def run(self):
        threadlock.acquire(); # 2. It means current running thread gets the lock all the thread are waiting.
        self.tableobj.print(self.number);
        threadlock.release();#3. It means realease the lock.

#To achieve the sychronization Before creating a Thread of shared resource object first of all lock the thread.
threadlock=Lock();#1.Lock the thread.
tableobj=Table();
t1=MyThread(tableobj,5)
t2=MyThread(tableobj,6)
t3=MyThread(tableobj,7)
t1.start();
t2.start();
t3.start();