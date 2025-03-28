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


# An asynchronous generator.
async def square_odds(start, stop):
    for odd in odds(start, stop):
        # Pretend to be taking time for this operation
        await asyncio.sleep(2)
        yield odd ** 2


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
    # Remember the expression, `(rand_number for...)`, is a **generator
    # expression**; that is, it returns a generator. Unpacking it,
    # using the `*` operator "expands" the generator into a
    # sequence of its results.
    r = await asyncio.gather(*(rand_number() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print(f'{r=} took {elapsed:0.2f} seconds')

    async for so in square_odds(11, 17):
        print(f'{so=}')


if __name__ == '__main__':
    asyncio.run(main())
