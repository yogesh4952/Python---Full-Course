class BankAccount:
    def __init__(self,inital_deposit):
        self.balance  =inital_deposit

    def print_balance(self):
        print(f'Balance: {self.balance}')
    def __add__(self,other):
        total = self.balance + other.balance
        return BankAccount(total)

account1 = BankAccount(2000);
account2 = BankAccount(1000);
new_account = account1 + account2;#Esto chai mildaina so we use add add is lke operator overloading

print(new_account.print_balance())