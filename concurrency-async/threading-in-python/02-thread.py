"""
Demonstrates potential issues arising from multiple threads.
"""

import time


def my_func():
    print('hello')
    # Introduce a "blocking call"
    time.sleep(10)
    return True


if __name__ == '__main__':
    my_func()
