#Exercise of function in python

#Exercise 1: Write a function that takes three numbers as parameters and returns the maximum of the three numbers.

def findmaximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(findmaximum(10, 50, 100))

#exercise 2: Write a function that takes a number as a parameter and returns the factorial of that number.

def factorial(number):
    if number == 0:
        return 1
    elif number > 0:
        fac = 1
        for i in range(1, number + 1):
            fac *= i
        return fac
    else:
        return f"Invalid input. Please enter a non-negative integer."

a = int(input("Enter a number to find its factorial: "))
print(factorial(a))