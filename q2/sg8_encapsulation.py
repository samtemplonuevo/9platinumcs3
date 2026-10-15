class BankAccount :
    def __init__ (self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        self.set_account_number(account_number)
        self.set_balance (balance)

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance (self, balance):
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = float(balance) 

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

a1 = BankAccount (12345, 1000)

print ("Account 1")
print (f"Account Number: {a1.account_number}")
print (f"Balance: {a1.balance:.2f}")
print()
print ("Update balance to -100")
a1.set_balance (-100)
print (f" Account Number: {a1.account_number}")
print (f"Balance: {a1.balance:.2f}")
