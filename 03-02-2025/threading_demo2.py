import threading #1
import time #2

print("Main thread started")

def single_task():
    print("Sub task started") #4
    time.sleep(2) #5
    print("Sub task completed") #6

#time.sleep(2)
thread=threading.Thread(target=single_task) #3
thread.start() #4
#thread.join() #7
print("Main thread execution completed") #8