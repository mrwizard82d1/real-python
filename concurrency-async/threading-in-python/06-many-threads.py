"""
Demonstrate many threads: the main threads waits for the other threads
"""

import threading
import time


def my_func_1(name):
    print(f'my_func_1() called with "{name}"')
    time.sleep(10)
    print('my_func_1() ended')
    return True


def my_func_2(name):
    print(f'my_func_2() called with "{name}"')
    time.sleep(10)
    print('my_func_2() ended')
    return True


def my_func_3(name):
    print(f'my_func_3() called with "{name}"')
    time.sleep(10)
    print('my_func_3() ended')
    return True


if __name__ == '__main__':
    print('main() started on main thread')
    # Create a daemon thread. A daemon thread **does** not keep the process running by default.
    t1 = threading.Thread(target=my_func_1, name='my_func_1', args=['foo'])
    t1.start()
    t2 = threading.Thread(target=my_func_2, name='my_func_2', args=['bar'])
    t2.start()
    t3 = threading.Thread(target=my_func_3, name='my_func_3', args=['baz'])
    t3.start()

    # Causes main thread to wait for `t` to finish before continuing.
    t1.join()
    t2.join()
    t3.join()

    print('main() ended on main thread')
