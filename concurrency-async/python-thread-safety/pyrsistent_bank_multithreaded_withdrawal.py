import time # For `sleep()`
from concurrent.futures import ThreadPoolExecutor

from pyrsistent import PClass, field


class BankAccount(PClass):
    balance = field(type=int)

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.1) # Simulate a delay
            result = self.set(balance=new_balance)
            return result
        else:
            raise ValueError('Insufficient funds')


account = BankAccount(balance=1000)


with ThreadPoolExecutor(max_workers=2) as executor:
    result_500 = executor.submit(account.withdraw, 500).result()
    result_700 = executor.submit(account.withdraw, 700).result()

print(f'Final balance: {account.balance}')
print(f'Final balance: {result_500.balance}')
print(f'Final balance: {result_700.balance}')
