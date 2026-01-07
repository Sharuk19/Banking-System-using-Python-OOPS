from banking_system import banking_system

class SavingsAccount(banking_system):
    MIN_BALANCE = 1000

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self._balance - amount >= self.MIN_BALANCE:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self._balance}")
        else:
            print("Insufficient balance. Minimum ₹1000 required.")