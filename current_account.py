from banking_system import banking_system

class CurrentAccount(banking_system):

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self._balance}")
        else:
            print("Insufficient funds.")