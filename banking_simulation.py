class Account:
    def __init__(self, account_number: str, account_holder: str, balance: float):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance}")
    
    def deposit(self, amount: float):
        if amount <= 0:
            print("\nWe can't deposit nothing or a negative amount")
            return False
        else:
            self.balance += amount
            print(f"\nYou have successfully deposited ${amount} into your bank account")
            print(f"\nUpdated balance: ${self.balance}")
            return True
    
    def withdraw(self, amount: float):
        if amount > self.balance:
            print(f"\nWe can't withdraw ${amount} as it represents more money than your current balance which is: ${self.balance}")
            return False
        else:
            self.balance -= amount
            print(f"\nYou have successfully withdrawn ${amount}")
            print(f"\nUpdated balance: ${self.balance}")
            return True
class SavingAccount(Account):
    def __init__(self, account_number: str, account_holder: str, balance: float, interest_rate: float):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance += self.balance*self.interest_rate
        print(f"\nThe interest rate has been applied, you now have {self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number: str, account_holder: str, balance: float, overdraft_limit: float):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount: float):
        if (self.balance - amount) < 0 and abs(self.balance - amount) > self.overdraft_limit:
            print(f"\nWe can't withdraw ${amount} because it would make your balance exceed the overdraft limit which is: ${self.overdraft_limit}")
            return False
        else:
            self.balance -= amount
            print(f"\nYou have successfully withdrawn ${amount}")
            if self.balance < 0:
                print(f"\nYou now owe this: ${abs(self.balance)}")
            else:
                print(f"\nUpdated balance: ${self.balance}")
            return True