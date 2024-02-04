class Account:
    pass
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, x):
        self.balance = self.balance + x
    def withdraw(self, y):
        if self.balance >= y:
            self.balance = self.balance - y
        else:
            print("There is not enough amount in the balance")

Acc1 = Account("Mansur", 10000)
Acc1.withdraw(11000)
print(Acc1.balance)
Acc1.deposit(6000)
Acc1.withdraw(10000)
print(Acc1.balance)