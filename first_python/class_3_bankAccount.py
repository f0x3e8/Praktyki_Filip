class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance <= 0 or amount > self.balance:
            return False
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("Adam")

account.deposit(100)
account.deposit(50)
print(account.get_balance())

account.withdraw(30)
print(account.get_balance())

print(account.withdraw(1000))
print(account.get_balance())
