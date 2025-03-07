import threading
import time

def even():
    for i in range(2,11,2):
        print(i,end=" ")
    print()
    time.sleep(2)

def odd():
    for i in range(1,11,2):
        print(i,end=" ")
    print()
    time.sleep(2)

t1=threading.Thread(target=even)
t2=threading.Thread(target=odd)
t1.start()
t2.start()
t2.join()
print("Numbers are printed")