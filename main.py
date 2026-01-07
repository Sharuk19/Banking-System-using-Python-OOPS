from savings_account import SavingsAccount
from current_account import CurrentAccount

def main():
    print("Choose account type (1. Savings  2. Current): ")
    acc_type = int(input())

    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Holder Name: ")
    balance = float(input("Enter Initial Balance: "))

    if acc_type == 1:
        account = SavingsAccount(acc_no, name, balance)
    else:
        account = CurrentAccount(acc_no, name, balance)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Show Details\n4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == 3:
            account.display_details()

        elif choice == 4:
            print("Thank you for banking with us.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()