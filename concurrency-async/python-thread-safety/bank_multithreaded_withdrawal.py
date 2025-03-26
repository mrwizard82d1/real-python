import time # For `sleep()`
from concurrent.futures import ThreadPoolExecutor


class BankAccount:
    def __init__(self, balance=0):
       self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            delay = 0.1 if amount == 500 else 5
            print(f'{delay=} for {amount=}')
            time.sleep(0.1 if amount == 500 else 0.5) # Simulate a delay
            self.balance = new_balance
            print(f'{self.balance=} for {amount=}')
        else:
            raise ValueError('Insufficient funds')


account = BankAccount(1000)


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(account.withdraw, 500)
    executor.submit(account.withdraw, 700)

print(f'Final balance: {account.balance}')
