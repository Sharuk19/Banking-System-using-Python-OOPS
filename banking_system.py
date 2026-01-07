from abc import ABC, abstractmethod

class banking_system(ABC):
    def __init__(self, account_number: int, holder_name: str, balance: float):
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")

    def display_details(self):
        print(f"Account No: {self._account_number}")
        print(f"Holder Name: {self._holder_name}")
        print(f"Balance: ₹{self._balance}")

    @abstractmethod
    def withdraw(self, amount: float):
        pass