"""
More realistic asynchronous example.
"""

import asyncio
import json
import time

import aiohttp


async def worker(name, n, session):
    """
    A worker function that collects n items
    :param name: The name of the session
    :param n: The number of items to request
    :param session: The HTTP session to use
    :return:
    """
    print(f'worker {name} started')
    url = f'https://www.random.org/integers/?num={n}&min=1&max=100000&col=1&base=10&format=plain&rnd=new'
    response = await session.request(method='GET', url=url)
    value = await response.text()
    return value

async def main():
    """
    Create session and run requests asynchronously.
    """
    async with aiohttp.ClientSession() as session:
        response = await worker(name='Bob', n=3, session=session)
        print(f'{response=}, type={type(response)}')


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'Executed in {elapsed:.2f} seconds')
