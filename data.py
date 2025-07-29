class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner          # public
        self.__balance = balance    # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

# Example usage:
account = BankAccount("Alice", 1000)
account.deposit(200)
account.withdraw(100)
print("Current Balance:", account.get_balance())

# Trying to access private attribute directly (not recommended)
print(f" Initial balance {account._BankAccount__owner}")  # Raises AttributeError

# Correct way (through name mangling)
print(f"Current Balance {account._BankAccount__balance}")
