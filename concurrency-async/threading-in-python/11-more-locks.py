import threading

lock = threading.Lock()
print('Acquiring a lock')
lock.acquire()
print('Lock acquired')
lock.release()
print('Lock released')
print('Acquiring a lock produces no deadlock')
lock.acquire()
print('Lock acquired')
