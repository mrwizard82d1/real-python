"""
Demonstrates using `threading.Semaphore` to limit access to a specific number of threads.
"""


from concurrent.futures import ThreadPoolExecutor
import random
import threading
import time
import logging


# Semaphore with a maximum of two resources (for example, bank tellers)
teller_semaphore = threading.Semaphore(2)


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)


def serve_customer(name):
    logging.info(f'{name} is waiting for a teller.')
    with teller_semaphore:
        logging.info(f'{name} is being served by a teller.')
        # Simulate the time taken for the teller to serve the customer
        time.sleep(random.randint(1, 3))
        logging.info(f'{name} is finished being served.')


customers = [
    'Customer 1',
    'Customer 2',
    'Customer 3',
    'Customer 4',
    'Customer 5',
]


with ThreadPoolExecutor(max_workers=5) as executor:
    for customer_name in customers:
        thread = executor.submit(serve_customer, customer_name)

logging.info('All customers have been served.')
