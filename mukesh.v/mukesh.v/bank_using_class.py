class Bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amt):

        self.balance+=amt
    def withdraw(self,amt):
        self.balance-=amt
    def display(self):
        print("balance",self.balance)
b1=Bank(balance=50000)

b1.deposit(1000)
b1.withdraw(500)
b1.display()
