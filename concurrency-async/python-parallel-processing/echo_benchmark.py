"""
Demonstrate exchanging large amounts of data between processes.
"""

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from codetiming import Timer

def echo(data):
    return data


if __name__ == '__main__':
    data = [complex(i, i) for i in range(15_000_000)]
    for executor in (ThreadPoolExecutor(), ProcessPoolExecutor()):
        with Timer(text=f'Time for {type(executor).__name__}={{:.5f}}') as timer:
            with executor:
                future = executor.submit(echo, data)
                future.result()
