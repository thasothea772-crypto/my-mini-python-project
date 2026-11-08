import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Year": [2023, 2024, 2025, 2026],
    "Cloud Servers": [1300, 1400, 1450, 1600],
    "Database Hosting": [1400, 1500, 1700, 2000],
    "Security Software": [1100, 1560, 1900, 2000],
    "Demain & SSL": [1000, 1200, 1400, 1600],
}

df = pd.DataFrame(data)

df["Total Cost"] = df["Cloud Servers"] + df["Database Hosting"] + df["Security Software"] + df["Demain & SSL"]
df["Avg Cost"] = df["Total Cost"]/4

print(df)

# 1. Show the result about Cloud Servers
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x="Year", y="Cloud Servers", data=df, palette="Blues_d")

plt.title("The Analysis Expenses On Cloud Servers (IT Economics)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Cloud Servers")

plt.show()

# 2. Show the result chart of Database Hosting
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x="Year", y="Database Hosting", data=df, palette="Blues_d")

plt.title("The Analysis Expenses On Database Hosting (IT Economics)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Database Hosting")

plt.show()

# 3. Show the result chart of Security Software
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x="Year", y="Security Software", data=df, palette="Blues_d")

plt.title("The Analysis Expenses On Security Software (IT Economics)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Security Software")

plt.show()

# 4. Show the result chart of Demain & SSL
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x="Year", y="Demain & SSL", data=df, palette="Blues_d")

plt.title("The Analysis Expenses On Demain & SSL (IT Economics)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Demain & SSL")

plt.show()

# 5. Show the result chart of Total Cost
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x="Year", y="Total Cost", data=df, palette="Blues_d")

plt.title("The Analysis Expenses On Total Cost (IT Economics)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Cost")

plt.show()
