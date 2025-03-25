import threading


semaphore = threading.Semaphore(50)
print(semaphore._value)
