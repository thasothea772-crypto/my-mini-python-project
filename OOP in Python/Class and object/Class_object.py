print("-----< Learn about class and object >-----")
class Kimsa:
    def __init__(self, name, beauty):
        self.name = name
        self.beauty = beauty

    def call(self):
        return f"{self.name} is calling me : babe babe...!"
    

my_girlfriend = Kimsa(name = "Kimsa", beauty = "She's so beautiful.")
 

print(my_girlfriend.name)
print(my_girlfriend.call())
print(my_girlfriend.beauty)

class Car:
    def __init__(self1, brand, model, year):
        self1.brand = brand
        self1.model = model
        self1.year = year

    def function(self1):
        return (f"{self1.model} can drift, race and auto drive.") 
    
    def color(self1):
        return (f"{self1.model} is black.")

car1 = Car(brand = "NISSAN", model = "GTR R34", year = 2008)
print(car1.brand)
print(car1.model)
print(car1.year)
print(car1.function())
print(car1.color())

print()
car2 = Car(brand = "Toyota", model = "Pruis", year = 2010)
print(car2.brand)
print(car2.model)
print(car2.year)
print(car2.function())
print(car2.color())

print()
print("----< Welcome to class and object int Python >----")

class Car:
    def __init__(self, brand, model, color, speed, years):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = speed 
        self.years = years
        
    def ft1(self):
        return (f"The function of {self.model} car it can auto drive and when you are near or close to something it will automatically tell you electronically by gaving a sound signal.")
    def ft2(self):
        return (f"Especially {self.model} car we can use it for racing or drift")
    def line(self):
        print("------------------------------------------------------------")
        
car1 = Car(brand = "BMW", model = "x5", color = "black", speed = "500km/h", years = 2016)
print(f"The brand of this car is {car1.brand}.")
print(f"It is {car1.model} car.")
print(f"Its color is {car1.color}.")
print(f"The speed of this car is {car1.speed}.")
print(f"The year that it was produced on {car1.years}.")
print()
print(car1.ft1())
print(car1.ft2())
print()
car1.line()