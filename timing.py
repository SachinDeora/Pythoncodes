import time;
initial=time.time();
print(initial);

k=0;
while(k<4):
    time.sleep(2);
    print(k);
    k=k+1;
print("while loop is over:-",time.time()-initial);

initial2=time.time();
for i in range(45):
    print(i);
print("time Over for loop :-",time.time()-initial2)

ase=time.asctime(time.localtime(time.time()));
print(ase);