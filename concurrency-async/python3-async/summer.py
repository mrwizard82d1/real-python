"""
More realistic asynchronous example.
"""

import asyncio
import json
import time

import aiohttp


async def main():
    pass


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'Executed in {elapsed:.2f} seconds')
