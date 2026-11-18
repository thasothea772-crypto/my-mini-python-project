import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [2020, 2021, 2022, 2023, 2024, 2025, 2026],
    'A': [1500, 1250, 2000, 2900, 1300, 2500, 1000],
    'B': [1100, 1200, 2030, 3000, 2000, 1500, 1000],
    'C': [2000, 4500, 3000, 1000, 2100, 2500, 3400],
    'D': [1020, 1000, 2300, 5000, 4900, 2100, 3050],
    'E': [3000, 1020, 3200, 1000, 2500, 4000, 4300],
}

df = pd.DataFrame(data)

print(df)

df['Total'] = df['A'] + df['B'] + df['C'] + df['D'] + df['E']
print(df)

sns.set_theme(style='whitegrid')

fig, axes = plt.subplots(3, 2, figsize=(14, 15))

sns.barplot(
    x='Year', y='A', data=df, ax=axes[0, 0], palette='Blues_d'
)
axes[0, 0].set_title('A Expenses')

sns.barplot(
    x='Year', y='B', data=df, ax=axes[0, 1], palette='Blues_d'
)
axes[0, 1].set_title('B Expenses')

sns.barplot(
    x='Year', y='C', data=df, ax=axes[1, 0], palette='Blues_d'
)
axes[1, 0].set_title('C Expenses')

sns.barplot(
    x='Year', y='D', data=df, ax=axes[1, 1], palette='Blues_d'
)
axes[1, 1].set_title('D Expenses')

sns.barplot(
    x='Year', y='E', data=df, ax=axes[2, 0], palette='Blues_d'
)
axes[2, 0].set_title('E Expenses')

sns.barplot(
    x='Year', y='Total', data=df, ax=axes[2, 1], palette='Reds_d'
)
axes[2, 1].set_title('Total Expenses')

plt.tight_layout()

plt.show()