"""
Demonstrates potential issues arising from multiple threads.
"""

def my_func():
    print('hello')
    return True


if __name__ == '__main__':
    my_func()
