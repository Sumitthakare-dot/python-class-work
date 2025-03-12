class ATM:
    def __init__(self,balance=0):
        self.balance = balance
    def check_balance(self):
        return self.balance
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -=amount
            return f"Withdrawal successful. Remaining balance:{self.balance}"
        else:
            return "Insufficient funds." 


atm = ATM(2000)
print(atm.withdraw(500))           