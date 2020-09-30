#Created by Shelley Ophir
#Coding Dojo Sep. 30, 2020
# Write a new BankAccount class.

# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. 
class BankAccount:
    def __init__(self, amount = 0, rate = 0.01):
        self.balance = amount

    # The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)
        self.rate = rate

# The class should also have the following methods:
# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount

        return self

# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdrawl(self, amount):
        if (self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        
        return self

# display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print("Balance:", self.balance)

# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if (self.balance > 0):
            self.balance = format(self.balance * (1 + self.rate), ".2f")
            #round to 2 decimal places
        
        return self


# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
account1 = BankAccount(rate = .03)
account1.deposit(10).deposit(30).deposit(60).withdrawl(40).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
account2 = BankAccount(rate = .05)
account2.deposit(80).deposit(45).withdrawl(1).withdrawl(3).withdrawl(5).withdrawl(18).yield_interest().display_account_info()