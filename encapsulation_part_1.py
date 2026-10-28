class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            print(f"{self.account_holder} deposit {amount}")
            self.__balance += amount
        else:
            print("Amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Balance must greater than zero and less than your current balance.")            
    def show_balance(self):
        print(self.__balance)

    @property
    def balance(self):
        return self.__balance 
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance can not be negative.")           

# customer = BankAccount("Waqas", 20000)
# customer.deposit(1000)
# customer.withdraw(5000)
# customer.withdraw(50000)
# customer.withdraw(-2000)
# customer.withdraw(0)
# customer.show_balance()
customer = BankAccount("Waqas", 20000)

print(customer.balance)

customer.balance = 25000
print(customer.balance)

customer.balance = -500
print(customer.balance)