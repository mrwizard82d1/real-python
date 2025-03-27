"""
Asynchronous (Non-Blocking) HTTP Calls
"""

import asyncio

import aiohttp
from codetiming import Timer


# Remember, `task()` is an **asynchronous** function
async def task(name, work_queue):
    # The timer for each iteration of the task loop
    timer = Timer(text=f'Task {name}: elapsed time: {{:.3f}}')
    # Creates an `aiohttp` **session** context manager
    # I need to add these two parameters to correct an error when querying google.com
    async with aiohttp.ClientSession(max_line_size=8190 * 2,
                                     max_field_size=8190 * 2) as session:
        while not work_queue.empty():
            # Creates an `aiohttp` **response** context manager
            # Gets resources from URL within that context manager
            url = await work_queue.get()
            print(f'Task {name}: getting URL: {url}')
            timer.start()
            # Uses the `session` to get the text from the URL **asynchronously**
            async with session.get(url) as response:
                await response.text()
            timer.stop()


async def main():
    # Create the queue of work to be done
    work_queue = asyncio.Queue()

    # Put some work in the queue
    urls = [
        'https://google.com',
        'https://yahoo.com',
        'https://linkedin.com',
        'https://apple.com',
        'https://microsoft.com',
        'https://facebook.com',
        'https://twitter.com',
    ]
    for url in urls:
        await work_queue.put(url)

    # Run the tasks
    with Timer(text='Total elapsed time: {:.3f}'):
        await asyncio.gather(
            *[asyncio.create_task(task(url, work_queue)) for url in urls],
        )


if __name__ == '__main__':
    asyncio.run(main())
