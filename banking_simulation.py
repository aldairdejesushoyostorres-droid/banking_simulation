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
        try:
            if amount <= 0:
                print("\nWe can't deposit nothing or a negative amount")
                return False
            else:
                self.balance += amount
                print(f"\nYou have successfully deposited ${amount} into your bank account")
                print(f"\nUpdated balance: ${self.balance}")
                return True
        except ValueError:
            print("\nError Message: You have to introduce a numeric value to be deposited!")
    
    def withdraw(self, amount: float):
        try:
            if amount > self.balance:
                print(f"\nWe can't withdraw {amount} as it represents more money than your current balance which is: {self.balance}")
                return False
            else:
                self.balance -= amount
                print(f"\nYou have successfully withdrawn ${amount}")
                print(f"\nUpdated balance: ${self.balance}")
                return True
        except ValueError:
            print("\nError Message: You have to introduce a numeric value to be deposited!")

#Testing Everythig

account1 = Account("1234567890", "Aldair Hoyos", 200000)
account1.display_balance()

account1.deposit(-200)
account1.deposit(1200)
account1.withdraw(400000)
account1.withdraw(100000)