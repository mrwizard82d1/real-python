"""
Cooperative Concurrency with Blocking Calls.
"""

import queue
import time

from codetiming import Timer


def task(name, work_to_be_done):
    timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')
    while not work_to_be_done.empty():
        delay = work_to_be_done.get()
        print(f'Task {name} running...')
        timer.start()
        time.sleep(delay) # Replaces the `for` loop in previous examples
        timer.stop()
        yield


def main():
    # Create the work queue
    work_queue = queue.Queue()

    # Put some work in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # Create workers (from generator functions)
    tasks = [task('One', work_queue), task('Two', work_queue)]

    # Run the tasks
    done = False
    with Timer(text='\nTotal elapsed time: {:.1f}'):
        while not done:
            for t in tasks:
                try:
                    next(t)
                except StopIteration:
                    tasks.remove(t)
                if len(tasks) == 0:
                    done = True


if __name__ == '__main__':
    main()
