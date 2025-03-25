import threading

lock = threading.Lock()
lock.acquire()
print('lock acquired')
# Anything between acquire and release is protected
lock.release()
print('lock released')
