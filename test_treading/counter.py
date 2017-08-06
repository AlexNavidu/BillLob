import threading
import time

counter = 0
lock = threading.Lock()

def inc():
    global counter
    lock.acquire()
    v = counter
    time.sleep(0.001)
    counter = v + 1

# будет хранить пул наших потоков
pool = []
for _ in range(1000):
    th = threading.Thread(target=inc)
    th.start()
    pool.append(th)

for th in pool:
    th.join()

print(counter)
