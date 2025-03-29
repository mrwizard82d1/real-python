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
    :param n: The number of random numbers to request
    :param session: The HTTP session to use
    :return: The returned data in JSON format
    """
    print(f'worker {name} started')
    url = 'https://api.random.org/json-rpc/4/invoke'
    params = {
        'jsonrpc': '2.0',
        'method': 'generateIntegers',
        'params': {
            'apiKey': 'cd0c0017-8bfd-44dc-80d1-183464ec75f8',
            'n': n,
            'min': 0,
            'max': 65535,
            'replacement': True
        },
        'id': 42,
    }
    response = await session.post(url,
                                  data=json.dumps(params),
                                  headers={'Content-Type': 'application/json'})
    value = await response.text()
    json_value = json.loads(value)
    return sum(json_value['result']['random']['data'])


async def main():
    """
    Create session and run requests asynchronously.
    """
    async with aiohttp.ClientSession() as session:
        sums = await asyncio.gather(*(worker(f'w{i}', n, session) for
                                      i, n in enumerate(range(2, 5))))
        print(f'{sums=}')


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'Executed in {elapsed:.4f} seconds')
