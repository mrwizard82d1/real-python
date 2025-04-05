"""
A `ctypes` module to calculate Fibonacci numbers.
"""

import ctypes
import os
import threading


fibonacci = ctypes.CDLL('./fibonacci.so')


for _ in range(os.cpu_count()):
    threading.Thread(target=fibonacci.fib, args=(45,)).start()
