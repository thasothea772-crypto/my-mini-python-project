#OOP: Encapsulation ==========================================================
#public, private, protected

class Person:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self.__age = age  # private attribute

    def get_age(self):  # public method to access private attribute
        return self.__age

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
per = Person(name, age)
print(f"Name: {per.name}")  # Accessing public attribute
print(f"Age: {per.get_age()}")  # Accessing private attribute through public method
