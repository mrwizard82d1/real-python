"""
Demonstrate two threads.
"""

import time


def my_func(name):
    print(f'my_func() called with {name}')
    time.sleep(10)
    print(f'my_func() called with {name} ended')
    return True

if __name__ == '__main__':
    print('main() started')
    my_func('realpython')
    print('main() ended')
