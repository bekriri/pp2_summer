# class methods

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            print("Withdrew:", amount)

    def show_balance(self):
        print(self.owner, "- balance:", self.balance)


acc = BankAccount("Bekri")
acc.deposit(1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)
acc.show_balance()
