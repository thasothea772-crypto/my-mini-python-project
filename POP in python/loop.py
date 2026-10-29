# loop in python
# for loop
for a in range(11):
    print("Number:", a)
print("\n")
for b in range(1, 11, 1):
    print(b)
print("\n")
for c in range(0, 12, 2):
    print(c)
print("\n")
for d in range(1, 12, 2):
    print(d)
print("\n")

student_list = ["Sothea", "Kimsa", "Serey Roth", "Pheaktra"]
for e in range(len(student_list)):
    print("Name", str(e + 1), ":", student_list[e])

print("\n")
students_list = ["Mao SeTong", "Jang kaijea", "Ju Englai", "Salon sor"]
for f, students in enumerate(students_list, start = 1):
    print("Name", str(f), ":", students)
print("\n")
for x, student in enumerate(students_list, start = 1):
    print(f"Name {x}: {student}")

print("\n")
for i in range(2, 11, 1):
    for j in range(1, 11, 1):
        print(f"{i} x {j} = {i*j}")

print("\n")
for g in range(1, 10, 1):
    if(g == 3):
        continue
    print(g)

print("\n")
for h in range(1, 11, 1):
    if(h == 7):
        break
    print(h)

# sum of number
print("\n")
number_list = [1, 2, 3, 4, 5]
total = 0
for y in range(len(number_list)):
    total = total + number_list[y]
print("Total: ", total)

print("\n")
number_list = [1, 2, 3, 4, 5]
total = 0
for r in range(len(number_list)):
    total = total + number_list[r]
print("Total: ", total)

print("\n")
price = [10, 25, 50, 80,110]
for z in range(len(price)):
    if (price[z] >= 50):
        print(f"price {price[z]} :Get a discount")
    else:
        print(f"price {price[z]} :it's simple price")

print("\n")
# while loop in python
k = 1
while k <= 4:
    print("Number:", k)
    k += 1
print("\n")
n = 1
while n <= 10:
    print("Number:", n)
    n += 1

print("\n")
correct_password = 1234
count = 0  
while count < 3:
    t = int(input("Input your password: "))
     
    if t == correct_password:
        print("Login successful. Welcome to the system.")
        break
    else:
        count += 1  
        print(f"Wrong password! {count}")

if count == 3:
    print("Your account is locked!")

x = 1
while True:
    if x == 4:
        break
    print(x)
    x += 1
    