"""
Demonstrates use of a threading.Condition() to avoid "busy waiting"
for a customer to arrive.
"""

from concurrent.futures import ThreadPoolExecutor
import logging
import random
import threading
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Create a `Condition` to be used later
customer_available_condition = threading.Condition()


# Customers awaiting a teller
customer_queue = []


def serve_customers():
    while True:
        with customer_available_condition:
            # Wait for customer to arrive
            while not customer_queue:
                logging.info('Teller is waiting for a customer.')
                customer_available_condition.wait()

            # Serve the customer
            customer = customer_queue.pop(0)
            logging.info(f'Teller is serving {customer}.')

        # Simulate the time taken to serve the customer
        time.sleep(random.randint(1, 5))
        logging.info(f'Teller has finished serving {customer}.')


def add_customer_to_queue(name):
    with customer_available_condition:
        logging.info(f'{name} has arrived at the bank.')
        customer_queue.append(name)

        customer_available_condition.notify()


customer_names = [
    'Customer 1',
    'Customer 2',
    'Customer 3',
    'Customer 4',
    'Customer 5',
]


with ThreadPoolExecutor(max_workers=6) as executor:
    teller_thread = executor.submit(serve_customers)
    for name in customer_names:
        # Simulate customers arriving at random intervals
        time.sleep(random.randint(1, 3))
        executor.submit(add_customer_to_queue, name)
