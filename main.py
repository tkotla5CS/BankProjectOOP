class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive and above 0")
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount:.2f}")
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawl amount must be positive and above 0")
        if amount > self.balance:
            raise ValueError("Withdrawl can't be completed, Funds too low")
        else:
            self.balance = self.balance - amount
            self.transaction_history.append(f"Withdraw: -${amount:.2f}")
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

    def get_balance(self):
        return f"Current balance: ${self.balance:.2f}"

    def get_transaction_history(self):
        return f"transaction history: {self.transaction_history}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.next_account_number = 1000

    def create_account(self, owner_name, initial_balance=0):
        account_number = self.next_account_number
        self.next_account_number += 1
        new_account = BankAccount(account_number, owner_name, initial_balance)
        self.accounts[account_number] = new_account
        return f"Account created successfully. Account number: {account_number}"

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_number]

    def list_accounts(self):
        return [(acc.account_number, acc.owner_name, acc.balance)
                for acc in self.accounts.values()]

# Main function should be outside the Bank class
def main():
    my_bank = Bank("Stonewell")
    print(my_bank.create_account("Alice Johnson", 1000))
    print(my_bank.create_account("Bob Smith"))

    # Get an account and perform operations
    try:
        account = my_bank.get_account(1000)
        print(account.deposit(500))
        print(account.withdraw(200))
        print(account.get_balance())
        print("\nTransaction History:")
        print(account.get_transaction_history())

    except ValueError as e:
        print(f"Error: {e}")

# This should also be outside the Bank class
if __name__ == "__main__":
    main()