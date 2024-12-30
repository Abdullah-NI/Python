class Account:    # is type ka hi first project ba lete hai
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance is",self.get_balance())


    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("total balance is",self.get_balance())

    def get_balance(self):
        return self.balance

a1=Account(2000,123)
print(a1.get_balance())
a1.debit(1000)
a1.credit(500)

a1.credit(10000000)
