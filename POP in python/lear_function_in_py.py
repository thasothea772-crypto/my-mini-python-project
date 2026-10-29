#How to make function in python.
print("----< Function >----")
#1. The function that has no return type and has no parameters.
def line1():
    print("------------------------")
line1()
print("This is a function that has no return type and has no parameters.")
print("I love Kimsa.")
line1()

#2. The function that has no return type but has parameters.
def line2(a, n):
    total2 = a*n
    total3 = a+n
    total4 = a-n
    total5 = a/n
    print(f"a*b = {total2}")
    print(f"a+b = {total3}")
    print(f"a-b = {total4}")
    print(f"a/b = {total5}")
line2(2, 3)
line2(10, 3)

def name(name):
    print(f"Helle! {name} How are you?")
    print(f"{name}: I'm fine.")
name("Kimsa")
name("Sothea")

def happy_birthday(name, age):
    print(f"Happy birthday to my aunt {name}!")
    print(f"She is {age}.")
happy_birthday("Sok Lai", 38)

def happy_bthday(name1, age1, hometown):
    print(f"Happy birthday to you {name1}!")
    print(f"You are {age1} years old.")
    print(f"You borned in {hometown}.")
    print(f"Wish you all the best!")
print()
happy_bthday("Mak Sok Lai", 38, "Takeo Province")
print()
happy_bthday("Kimsa", 16, "Kandal Province")
print()
happy_bthday("Sothea", 20, "Phnom Penh")
print()



#3. The function that has return type and has parameters.
def add_number(x, y):
    result = x + y
    return result
result = add_number(10, 10)
print(result)

def cal(*subject):
    total = sum(subject)
    return total
total = cal(50, 50, 50)
print("Total: ",total)

def findarea(width, height):
    total6 = width*height
    return total6
total6 = findarea(10.3, 25.8)
print(f"S = {total6}")