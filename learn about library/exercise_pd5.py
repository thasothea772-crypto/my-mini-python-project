import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [2023, 2024, 2025, 2026],
    'Cloud Servers': [1300, 1400, 1450, 1600],
    'Database Hosting': [1400, 1500, 1700, 2000],
    'Security Software': [1100, 1560, 1900, 2000],
    'Domain & SSL': [1000, 1200, 1400, 1600],
}

df = pd.DataFrame(data)

# Calculate the total cost
df['Total Cost'] = (
    df['Cloud Servers']
    + df['Database Hosting']
    + df['Security Software']
    + df['Domain & SSL']
)
df['Avg Cost'] = df['Total Cost'] / 4

# Define the graphic structure
sns.set_theme(style='whitegrid')

# Create the large table that it's a local for showing 5 graphics (3 rows and 2 columns)
fig, axes = plt.subplots(3, 2, figsize=(14, 15))

# 1. Cloud Server Graphics
sns.barplot(
    x='Year', y='Cloud Servers', data=df, ax=axes[0, 0], palette='Blues_d'
)
axes[0, 0].set_title('Cloud Servers Expenses')

# 2. Database Hosting Graphics
sns.barplot(
    x='Year', y='Database Hosting', data=df, ax=axes[0, 1], palette='Blues_d'
)
axes[0, 1].set_title('Database Hosting Expenses')

# 3. Security Software Graphics
sns.barplot(
    x='Year', y='Security Software', data=df, ax=axes[1, 0], palette='Blues_d'
)
axes[1, 0].set_title('Security Software Expenses')

# 4. Domain & SSL Graphics
sns.barplot(
    x='Year', y='Domain & SSL', data=df, ax=axes[1, 1], palette='Blues_d'
)
axes[1, 1].set_title('Domain & SSL Expenses')

# 5. Total Cost Graphics
sns.barplot(x='Year', y='Total Cost', data=df, ax=axes[2, 0], palette='Reds_d')
axes[2, 0].set_title('Total IT Expenses')

# Delete(2,1) ចោលដើម្បីកុំឱ្យវាទទេស្អាត
fig.delaxes(axes[2, 1])

# Prepare the gab of each graphics
plt.tight_layout()

# The Showing all of Graphics
plt.show()
