"""
Demonstrates using `threading.Semaphore` to limit access to a specific number of threads.
"""


from concurrent.futures import ThreadPoolExecutor
import random
import threading
import time


# Semaphore with a maximum of two resources (for example, bank tellers)
teller_semaphore = threading.Semaphore(2)


def now():
    return time.strftime('%H:%M:%S', time.localtime())


def serve_customer(name):
    print(f'{now()}: {name} is waiting for a teller.')
    with teller_semaphore:
        print(f'{now()}: {name} is being served by a teller.')
        # Simulate the time taken for the teller to serve the customer
        time.sleep(random.randint(1, 3))
        print(f'{now()}: {name} is finished being served.')


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

print(f'{now()}: All customers have been served.')
