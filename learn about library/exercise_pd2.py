import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ១. បង្កើតទិន្នន័យ (Data)
data = {
    "Tool_Name": [
        "Cloud Server",
        "Database",
        "Security Software",
        "Domain & Hosting",
    ],
    "Category": ['Infrastructure', 'Infrastructure', 'Security', 'Network'],
    "Monthly_Cost": [400, 250, 120, 30],
    "Users_Count": [150, 150, 300, 300],
}

df = pd.DataFrame(data)

print(df)
print()
# TODO: 2. បង្កើតជួរឈរ Annual_Cost និងគណនា sum/mean
# ... សរសេរកូដរបស់អ្នកទីនេះ ...
annual_cost = df["Monthly_Cost"].sum()
print(f"Annual_Cost: {annual_cost}")
print()
# TODO: 3. ត្រងទិន្នន័យ Monthly_Cost > 100
# ... សរសេរកូដរបស់អ្នកទីនេះ ...
high_monthly_cost = df[df["Monthly_Cost"] > 100]
print("======= highest expenditure of monthly cost ======")
print(high_monthly_cost)

# TODO: 4. គូរក្រាហ្វិក និងរក្សាទុកជា PNG
# ... សរសេរកូដរបស់អ្នកទីនេះ ...
sns.set_theme(style='whitegrid')

# 3. Draw the bar graphic (Bar Plot) by pulled data from DataFrame (df)
plt.figure(figsize=(8, 5))
sns.barplot(x='Tool_Name', y='Monthly_Cost', data=df, palette='Blues_d')

# 4. Graphic tittle and letter
plt.title('The Analysis expenses on Cloud (IT Economics)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Expenses ($)', fontsize=12)

# 5. Show the graphic on the screen
plt.show()