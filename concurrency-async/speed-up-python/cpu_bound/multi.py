import multiprocessing
import time


def calculate(limit):
    return sum(i * i for i in range(limit))


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(calculate, numbers)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]

    print('Starting calculations...')
    start = time.time()
    find_sums(numbers)
    duration = time.time() - start
    print(f'Duration: {duration} seconds')
