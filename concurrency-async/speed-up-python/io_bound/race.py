# REMEMBER: the video reported that the Python interpreter made a
# change to the implementation of the GIL in Python in 2024, the
# code demonstrated in the video **no longer** exhibits the race
# condition.

from concurrent.futures import ThreadPoolExecutor


counter = 0


def change_counter(amount):
    global counter
    for _ in range(10_000):
        counter += amount


def race(num_threads):
    global counter
    counter = 0
    data = [-1 if x % 2 else 1 for x in range(1000)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(change_counter, data)

    print(counter)
