"""
Demonstrate deadlock by a single thread attempting to acquire a single lock **twice**.
"""


from concurrent.futures import ThreadPoolExecutor
import threading
import time


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        print(f'Thread {threading.current_thread().name} '
              'waiting to acquire lock for `deposit()`')
        with self.lock:
            print(f'Thread {threading.current_thread().name} '
                  'acquired lock for `deposit()`')
            time.sleep(0.1)
            self._update_balance(amount)

    def _update_balance(self, amount):
        print(f'Thread {threading.current_thread().name} '
              'waiting to acquire lock for `_update_balance()`')
        with self.lock:
            print(f'Thread {threading.current_thread().name} '
                  'acquired lock for `_update_balance()`')
            self.balance += amount

account = BankAccount()


with ThreadPoolExecutor(max_workers=3) as executor:
    for _ in range(3):
        executor.submit(account.deposit, 100)

print(f'Final account balance: {account.balance}')
