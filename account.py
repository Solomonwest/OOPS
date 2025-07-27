class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > 5:
            self.balance -= amount
            print (f"{self.name} your balance is {self.balance}")
        else:
            print("Insufficient funds")
        
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
    
class SavingsAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    """    def withdraw(self, amount):
        if amount <= 10000:
            return super().withdraw(amount)
        else:
            print ("Exceeded Limit")"""
        
    def deposit(self, amount):
        if amount > 0:
            return super().deposit(amount)
    

user1 = SavingsAccount('Solomon', 50000)
user1.withdraw(1000)

user1.deposit(9000)