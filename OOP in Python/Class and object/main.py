# OOP in Python ==========================================
class BankAccount:
    def __init__(self, owner, password1, balance):
        self.owner = owner
        self.password1 = password1
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return f"Your deposit amount: ${amount}."
name = "Tha Sothea"
password2 = 110532
owner = str(input("Enter your name\t : "))
password1 = int(input("Enter your ID\t : "))
if (owner == name and password1 == password2):
    print("=====Welcome your system=====")
    customer = BankAccount(owner, password1, 2000)
    print(f"Name\t\t : {customer.owner}")
    print(f"ID\t\t : {customer.password1}")
    print()
    print(f"Your Cash Balance: ${customer.balance}")
    deposit_amount = float(input("Your Deposited\t : $"))
    customer.deposit(deposit_amount)
    print(f"Your Deposit\t : ${customer.balance}")
elif (owner != name and password1 == password2):
    print("Wrong name! Please login again.")
elif (owner == name and password1 != password2):
    print("Wrong Password! Please login again.")
elif (owner != name and password1 != password2):
    print("Wrong name and Password! Please login again.")
