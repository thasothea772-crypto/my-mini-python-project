#OOP: inheritance ==========================================================
class Person:
    def __init__(self, name, id, age, gender):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender

    def show(self):
        print(f"Name: {self.name}")
        print(f"id: {self.id}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

class Student(Person):
    pass

students = Student("Tha Sothea", 11, 20, "Male")
print(f"Name: {students.name}")
print(f"ID: {students.id}")
print(f"Age: {students.age}")
print(f"Gender: {students.gender}")
#one more
print()
students.show()
