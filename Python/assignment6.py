# Laboratory Assignment: Python Class and Function
# Problem 1: Bank Account System

# You need to create a simple banking system that simulates various banking operations like deposit, withdraw, and checking balance using object-oriented programming.

# Instructions:

# Create a class BankAccount with the following attributes:

# account_number
# account_holder_name
# balance
# Implement the following methods in the class:

# deposit(amount) – Adds the specified amount to the balance.
# withdraw(amount) – Subtracts the specified amount from the balance if the balance is sufficient. If not, display an error message.
# check_balance() – Returns the current balance of the account.
# transfer_funds(amount, other_account) – Transfers funds to another account if the balance is sufficient.
# Create a subclass SavingsAccount which inherits from BankAccount and adds the following:

# interest_rate – The annual interest rate for the savings account.
# A method to calculate and add interest to the balance.
# Create instances of BankAccount and SavingsAccount and demonstrate the operations of both.


class BankAccount:
    def __init__(self,account_number,account_holder_name,balance=0) :
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.balance=balance
    def deposit(self):
        ammount=float(input("Enter The ammount to be added: "))
        self.balance+=ammount
        print(f"The Ammount {ammount} is added Successfully And the balance is now {self.balance}")
    def withdraw(self):
        ammount=float(input("Enter The ammount to withdraw: "))
        if(self.balance<ammount):
            print("Insufficient Balance .")
        else:
            self.balance-=ammount
            print(f"The Ammount {ammount} is withdrawn Successfully And the balance is now {self.balance}")
    def check_balance(self):
        print(f"Your Current Balance is {self.balance}")
    def transfer_funds(self):
        ammount=float(input("Enter The ammount to do transfer : "))
        new_acc=int(input("The The account number to do transfer fund :"))
        if(self.balance<ammount):
            print("Insufficient Balance .")
        else:
            self.balance-=ammount
            print(f"The {ammount} is succesfully transfer in the account {new_acc} . Your current Balance is : {self.balance}")
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance,interset_rate=3):
        super().__init__(account_number, account_holder_name, balance)
        self.interst_rate=interset_rate
    def add_interest(self):
        self.balance+=(self.balance*self.interst_rate/100)
        print(f"Interest added. New balance is {self.balance}")

account1=BankAccount(123456789,'Dsaha',1000)
account1.check_balance()
account1.withdraw()
account1.deposit()
account1.transfer_funds()

savingsacc=SavingsAccount(1234565559,'Saha',1000)
savingsacc.add_interest()



