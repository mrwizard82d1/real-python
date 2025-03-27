"""
Cooperative Concurrency with Non-Blocking Calls (using `async`/`await`).
"""

import asyncio

from codetiming import Timer


# The `task` function is no longer a generator; it is **asynchronous**
async def task(name, work_queue):
    # Timer for each loop iteration
    timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')
    # When `timer` goes out of scope, it will print the `text` to the console

    while not work_queue.empty():
        delay = await work_queue.get()
        print(f'Task {name} running...')
        # Start "work timer"
        timer.start()
        # A call to `asyncio.sleep` **does not block** unlike (`time.sleep`)
        await asyncio.sleep(delay)
        # Stops timer
        timer.stop()


async def main():
    # Create the **non-blocking, asynchronous** queue of work
    work_queue = asyncio.Queue()

    # Put some work in the queue using `await`
    for work in [15, 10, 5, 2]:
        await work_queue.put(work)

    # Create the two tasks and wait for them to finish (`asyncio.gather`)
    with Timer(text='Total elapsed time: {:.1f}'):
        await asyncio.gather(
            asyncio.create_task(task('One', work_queue)),
            asyncio.create_task(task('Two', work_queue)),
        )


if __name__ == '__main__':
    asyncio.run(main())
