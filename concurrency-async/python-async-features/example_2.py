"""
Cooperative concurrency using `yield`.
"""

import queue


def task(name, to_do_queue):
    while not to_do_queue.empty():
        count = to_do_queue.get()
        total = 0
        print(f'Task {name} running with {count} tasks.')
        for _ in range(count):
            total += 1
            yield
        print(f'Task {name} {total=}.')


def main():
    # Create a queue of work
    work_queue = queue.Queue()

    # Put some work on the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # Create some tasks
    print('Creating two "tasks" (actually **generators**) to do work.')
    task_names = ['One', 'Two']
    tasks = [task('One', work_queue), task('Two', work_queue)]
    print('Both generators have been created.')

    # Run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                print(f'Removing task {task_names[tasks.index(t)]} for lack of work.')
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == '__main__':
    main()
