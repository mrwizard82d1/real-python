"""
Synchronous (blocking) HTTP calls.
"""

import queue

from codetiming import Timer
import requests


def task(name, work_queue):
    # Measure the time of each iteration of the task loop (from `main`)
    timer = Timer(text=f'Task {name} elapsed time: {{:.2f}}')
    with requests.Session() as session:
        while not work_queue.empty():
            url = work_queue.get()
            print(f'Task {name}: getting URL: {url}')
            timer.start()
            # Introduces a (real) delay: reading a remote resource
            session.get(url)
            # Stops the timer and outputs the elapsed time since `timer.start()`
            timer.stop()
            yield


def main():
    # Create the queue of work
    work_queue = queue.Queue()

    # Put some work in the queue
    for url in [
        'https://google.com',
        'https://yahoo.com',
        'https://linkedin.com',
        'https://apple.com',
        'https://microsoft.com',
        'https://facebook.com',
        'https://twitter.com',
    ] :
        work_queue.put(url)

    # "Tasks" to be completed
    tasks = [task('One', work_queue), task('Two', work_queue)]

    # Run the tasks
    done = False
    with Timer(text='Total elapsed time: {:.1f}'):
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
