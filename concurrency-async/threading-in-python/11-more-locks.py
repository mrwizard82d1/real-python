import threading

lock = threading.Lock()
print('Acquiring a lock')
lock.acquire()
print('Lock acquired')
print('Acquiring a lock **again** produces deadlock')
lock.acquire()
print('Lock acquired')
