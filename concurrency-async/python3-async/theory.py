import asyncio
from random import randint
import time


def odds(start, stop):
    """
    Produces a sequence of odd numbers between start and stop, inclusive.

    :param start: The first value of the sequence
    :param stop: The last value of the sequence
    :return: A generated sequence
    """

    for odd in range(start, stop + 1, 2):
        # `yield` will return a value and "pause>
        yield odd


# **Asynchronous** version
async def rand_number():
    # Sleep but allow other "threads" to proceed
    await asyncio.sleep(3)
    return randint(1, 10)


async def main():
    odd_values = [odd for odd in odds(3, 15)]
    print(odd_values)
    odds2 = tuple(odds(21, 29))
    print(odds2)

    start = time.perf_counter()
    r = await rand_number()
    elapsed = time.perf_counter() - start
    print(f'{r=} took {elapsed:0.2f} seconds')

    start = time.perf_counter()
    r = await asyncio.gather(rand_number(), rand_number(), rand_number())
    elapsed = time.perf_counter() - start
    print(f'{r=} took {elapsed:0.2f} seconds')

if __name__ == '__main__':
    asyncio.run(main())
