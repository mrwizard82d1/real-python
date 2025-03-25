import threading


semaphore = threading.Semaphore(50)
semaphore.acquire()
semaphore.acquire()
semaphore.acquire()
semaphore.release()
print(semaphore._value)
