class BankAccount:
   starting_balance = 0.00
 
   def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name
 
   def deposit(self, starting_balance, amount):
       balance = starting_balance + amount
       return balance
  
   def withdraw(self, balance, amount):
       try:
           balance = balance - amount
       except balance <= 0.00:
           raise ValueError('Transaction declined. Insufficient funds. Deposit some money first.')
           withdraw(self, balance, amount)
       else:
           return balance