from tokenize import String


print("=======<Multi Variable>=======")
fruit = ["apple", "banana", "cherry"]
x, y, z = fruit
print(x)
print(y)
print(z)

x = y = z = "peach"
print(x)
print(y)
print(z)


# syntax in fstring.
fname = "Tha"
lname = "Sothea"
print("My name is", f"{fname} {lname}")

print(len(lname))
print(lname.upper())
print(lname.lower())

string = "hello world"
print(string.title())
print(string.split())

print(lname[0])
print(lname[0:6])