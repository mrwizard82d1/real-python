"""
Demonstrates using threading.Barrier.

This code waits for three tellers to be ready to service customers
and then the tellers service the customers.
"""
import threading
from concurrent.futures import ThreadPoolExecutor
import logging
import random
import time


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


teller_barrier = threading.Barrier(3)


def prepare_for_work(name):
    """The teller named `name` prepares for work."""

    logging.info(f'{name} is preparing their counter.')

    # Simulate the delay to prepare the counter
    time.sleep(random.randint(1, 3))
    logging.info(f'{name} has finished preparing.')

    # Wait for **all** tellers to finish preparing.
    teller_barrier.wait()
    logging.info(f'{name} is now ready to serve customers.')


tellers = [
    'Teller 1',
    'Teller 2',
    'Teller 3',
]


with ThreadPoolExecutor(max_workers=3) as executor:
    for teller_name in tellers:
        executor.submit(prepare_for_work, teller_name)


logging.info('All tellers are ready to serve customers.')
