"""
Demonstrate many threads using `concurrent.futures.ThreadPoolExecutor`
"""

import concurrent.futures
import time


def my_func_(name):
    print(f'my_func_() called with "{name}"')
    time.sleep(10)
    print(f'my_func_() ended with "{name}"')
    return True


if __name__ == '__main__':
    print('main() started')
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Creates three threads running `my_func()` with three different
        # arguments: 'foo', 'bar', and 'baz'.
        # Create(), start(), and join() effectively executed "under the hood".
        executor.map(my_func_, ['foo', 'bar', 'baz'])
    print('main() ended')
