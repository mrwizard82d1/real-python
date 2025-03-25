"""
Demonstrate two threads: a main thread and a daemon thread.
"""

import threading
import time


def my_func(name):
    print(f'my_func() called with "{name}"')
    time.sleep(10)
    print('my_func() ended')
    return True

if __name__ == '__main__':
    print('main() started on main thread')
    # Create a daemon thread. A daemon thread **does** not keep the process running by default.
    t = threading.Thread(target=my_func, name='my_func', args=['realpython'], daemon=True)
    t.start()
    print('main() ended on main thread')
