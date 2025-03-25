"""
Use `lock()` to control access to a critical section of our code.
"""

import threading

lock = threading.Lock()
lock.acquire()
print(lock)
lock.release()
print(lock)
