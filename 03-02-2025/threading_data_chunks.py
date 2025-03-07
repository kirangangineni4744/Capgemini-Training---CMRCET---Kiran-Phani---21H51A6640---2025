import threading
import time 

results=[]
def calc_sum(chunk):
    result=sum(chunk)
    results.append(result)

chunks=[
    list(range(10000)),
    list(range(10000,20000)),
    list(range(20000,30001)),
]

threads=[]

for chunk in chunks:
    thread=threading.Thread(target=calc_sum,args=(chunk,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
print(sum(results))