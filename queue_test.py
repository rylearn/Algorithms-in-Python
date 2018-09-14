
import Queue 
import threading
import time

def do_work(some_item):
	r_lock.acquire()
	print(some_item)
	r_lock.release()

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

def source():
	return [i for i in range(1000)]

start_time = time.time()
r_lock = threading.RLock()
q = Queue.Queue()
num_worker_threads = 5
for i in range(num_worker_threads):
     t = threading.Thread(target=worker)
     t.daemon = True
     t.start()

for item in source():
    q.put(item)

q.join() 
end_time = time.time()
print(end_time - start_time)
