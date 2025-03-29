"""
Python multiprocessing with multiple processes.
"""

import multiprocessing


def fib(n):
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    for _ in range(multiprocessing.cpu_count()):
        multiprocessing.Process(target=fib, args=(35,)).start()
