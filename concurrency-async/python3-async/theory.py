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

    r = await rand_number()
    print(f'{r=}')


if __name__ == '__main__':
    await main()
