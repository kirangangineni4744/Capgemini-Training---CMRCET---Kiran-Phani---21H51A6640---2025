import threading
import time
import requests
import queue

def producer(q):
    for i in range(5):
        time.sleep(1)
        q.put(1)
        print("Produced:",i)

def consumer(q):
    while True:
        item=q.get()
        if item is None:
            break
        print("Consumed:",item)
        time.sleep(2)

q=queue.Queue()
producer_thread=threading.Thread(target=producer,args=(q,))
consumer_thread=threading.Thread(target=consumer,args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)
consumer_thread.join()
print("Thread communication completed")