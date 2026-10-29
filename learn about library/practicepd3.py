import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Create the data's table (DataFrame)
data = {
    'Year': [2023, 2024, 2025, 2026],
    'Cloud_Cost': [5000, 7000, 9500, 12000],
}
df = pd.DataFrame(data)

# 2.define the structure of graphic (Seaborn Theme)
sns.set_theme(style='whitegrid')

# 3. Draw the bar graphic (Bar Plot) by pulled data from DataFrame (df)
plt.figure(figsize=(8, 5))
sns.barplot(x='Year', y='Cloud_Cost', data=df, palette='Blues_d')

# 4. Graphic tittle and letter
plt.title('The Analysis expenses on Cloud (IT Economics)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Expenses ($)', fontsize=12)

# 5. Show the graphic on the screen
plt.show()
