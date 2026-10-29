import numpy as np
import pandas as pd

student_data = {
    "Name": ["Tha Sothea", "Vy Sokimsa", "Sun Sereyroth", "Chhun Sopheak", "Pov Soklai"],
    "Score": [85, 99, 78, 92, 88],
}

df = pd.DataFrame(student_data)
index = np.argmax(df["Score"])   # index of highest score
lowest = np.argmin(df["Score"])  # index of lowest score
grade = []
for i in df["Score"]:
    if i >= 90:
        grade.append("A")
    elif i >= 80:
        grade.append("B")
    elif i >= 70:
        grade.append("C")
    else:
        grade.append("D")
df["Grade"] = grade

print(f"Top Student name: {df.loc[index, 'Name']}")
print(f"Highest Score: {df.loc[index, 'Score']}")
print(f"Lowest Student name: {df.loc[lowest, 'Name']}")
print(f"Lowest Score: {df.loc[lowest, 'Score']}")
