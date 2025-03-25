"""
Demonstrated concurrent access to state.
"""

import concurrent.futures
import time


class Account:
    def __init__(self):
        self.balance = 100  # shared data

    def update(self, transaction, amount):
        # When our two threads run, the deposit thread reads `self.balance`
        # which equals 100. Unfortunately, when the withdrawal thread runs,
        # it **also** reads `self.balance` **when it equals 100**. When the
        # deposit thread finishes, it sets `self.balance` to 150 as expected.
        # However, the withdrawal thread is unaware of the changed balance
        # and still thinks the balance is 100. It then subtracts the
        # transaction amount resulting in a(n incorrect) reported balance
        # of -50.
        print(f'{transaction} thread updating...')
        local_copy = self.balance
        local_copy += amount
        time.sleep(1)
        self.balance = local_copy
        print(f'{transaction} thread finishing...')


if __name__ == '__main__':
    account = Account()
    print(f'Starting with balance: {account.balance}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for transaction, amount in [('deposit', 50), ('withdrawal', -150)]:
            executor.submit(account.update, transaction, amount)
    print(f'Ending with balance: {account.balance}')
