# test pandas library part 3
import pandas as pd

def line(a):
    print(f"=========== {a} ===========")

def lines():
    print("========================================")

def liness(b):
    print(f"=== {b} ===")

data = {
    "Name": ["Tha Sothea", "Vy Sokimsa", "Van Kimgong", "Ven Saphorn", "Phorn Reaksa"],
    "Age": [20, 16, 18, 21, 20],
    "Score": [92, 95, 90, 85, 80],
    "City": ["Phnom Penh", "Takeo", "Svay Reang", "Prey Veng", "Koh Kong"]
}

df = pd.DataFrame(data)
print()
line("Student's System")
print(df)
lines()
print()

liness("Name and Age")
print(df[["Name", "Age"]])

print()
line("  Top Student  ")
top_student = df[df["Score"] >= 90]
print(f"{top_student}")
print()

total_score = df["Score"].sum()
print(f"The Total Score of all student: {total_score}")
avg_score = df["Score"].mean()
print(f"The Average Score of all student: {avg_score}")