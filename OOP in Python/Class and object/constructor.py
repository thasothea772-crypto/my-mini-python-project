#OOP in python: constructor ===========================================
class BankAccount:
    def __init__(self, owner, id, balance):
        self.owner = owner
        self.id = id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
           return f"Your deposit amount: ${amount}."

owner = str(input("Enter the account owner's name  : "))
id = int(input("Enter your ID\t\t\t: "))
balance = float(input("Enter the initial balance\t: $"))
print(f"Your balance\t\t\t: ${balance}")
customer = BankAccount(owner, id, balance)
deposit_amount = float(input("Enter the amount to deposit\t: $"))
print(f"Your deposit amount\t\t: ${deposit_amount}")
customer.deposit(deposit_amount)
print(f"Customer's name\t\t\t: {customer.owner}")
print(f"Customer's ID\t\t\t: {customer.id}")
print(f"Customer's balance\t\t: ${customer.balance}")


print("\n")

#Exercise

class BankAcc:
    def __init__(self, owner, id, balance):
        self.owner = owner
        self.id = id
        self.balance = balance
         
    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            return self.balance
        else:
            return f"Your deposit amount: ${amount}"
            
name = "Tha Sothea"
password = 110532
owner = str(input("Enter your name\t : "))
id = int(input("Enter your id\t : "))
if (owner == name and id == password):
    print("=====Welcome your system=====")
    customer = BankAcc(owner, id, 2000)
    print(f"Name\t\t : {customer.owner}")
    print(f"ID\t\t : {customer.id}")
    print()
    print(f"Your Cash Balance: ${customer.balance}")
    deposit_amount = float(input("You Deposited\t : $"))
    customer.deposit(deposit_amount)
    print(f"Your Deposit\t : ${customer.balance}")
elif (owner != name and id == password):
    print("Wrong name! Please login again.")
elif (owner == name and id != password):
    print("Wrong id! Please login again.")
elif (owner != name and id != password):
    print("Login Failed! Please try again.")
