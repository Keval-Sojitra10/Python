class Account:
    def __init__(self, bal, accno):
        self.bal = bal
        self.accno = accno

    def debit(self,amount):
        self.bal -= amount
        if amount > self.bal:
            print("Low balance")
        else:
            print( "Rs.",amount, "has been debited, current bank balance:Rs. ", self.bal)

    def credit(self,amount):
        self.bal += amount
        print( "Rs.",amount, "has been credited, current bank balance:Rs. ", self.bal)
balance = int(input("Enter your balance in account: "))
accountno = int(input("Enter your account number: "))
acc1 = Account(balance, accountno)
deb = int(input("Enter the amount to be debited: "))
acc1.debit(deb)
cred = int(input("Enter the amount to be credited: "))
acc1.credit(cred)
