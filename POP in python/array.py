#learn about array in python.
print("----< Array >----")
cars_model = ["Toyota", "Ford", "Mazda", "Masdas", "Lexus", "NISSAN"]
print(cars_model[0], "\t: $15000-$30000")
print(cars_model[1], "\t: $30000-$50000")
print(cars_model[2], "\t: $40000-$60000")
print(cars_model[3], "\t: $50000-$70000")
print(cars_model[4], "\t: $60000-$80000")
print(cars_model[5], "\t: $70000-$90000")

client_name = str(input("What car would you like to know about?: "))
print(f"Price of {client_name} is: ", end = "")
if client_name == "Toyota":
    print("$15000-$30000")
elif client_name == "Ford":
    print("$30000-$50000")
elif client_name == "Mazda":
    print("$40000-$60000")
elif client_name == "Masdas":
    print("$50000-$70000")
elif client_name == "Lexus":
    print("$60000-$80000")
elif client_name == "NISSAN":
    print("$70000-$90000")


print("\n")
for a in range(0, 6, 1):
    print(cars_model[a])

print("\n")
for b, cars_Model in enumerate(cars_model, start = 1):
    print("Car Model", str(b),":", cars_Model)

print("\n")
for c, Cars_Model in enumerate(cars_model, start = 1):
    print(f"Car Model {c}: {Cars_Model}")

cars_model.append("Honda")
print("\n")
for d, Cars_Model in enumerate(cars_model, start = 1):
    print(f"Car Model {d}: {Cars_Model}")

print("\n")
cars_model.remove("Mazda")
for e, Cars_Model in enumerate(cars_model, start = 1):
    print(f"Car Model {e}: {Cars_Model}")

print("\n")
cars_model.insert(2, "Mitsubishi")
for f, Cars_Model in enumerate(cars_model, start = 1):
    print(f"Car Model {f}: {Cars_Model}")

print("\n")
cars_model[0] = "BMW"
for g, Cars_Model in enumerate(cars_model, start = 1):
    print(f"Car Model {g}: {Cars_Model}")

print("\n")
student_list = ["Sothea", "Kimsa", "Mr.Roth", "Mr.Pheaktra"]
for h, student in enumerate(student_list, start =1):
    print(f"student {h}: {student}")

