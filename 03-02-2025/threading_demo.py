import threading #1
import time      #2

def single_task():
    print("Task has started") #4
    time.sleep(2) #5
    print("Task has ended") #6
    
#time.sleep(2)
thread=threading.Thread(target=single_task) #3
thread.start() #4
thread.join() #7
print("Main thread execution completed") #8