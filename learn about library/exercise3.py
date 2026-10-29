import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Tool": [
        "Cloud Servers",
        "Database Hosting",
        "Security Software",
        "Demain & SSL"
    ],
    "Category": [
        "Infrastructure",
        "Infrastructure",
        "Security",
        "Network"
    ],
    "Cost": [1500, 1700, 1000, 900]
}

df = pd.DataFrame(data)

print("================== Data ==================")
print(df)
print()
total_cost = df["Cost"].sum()
print(f"The Total Cost: ${total_cost}")

print()
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x="Tool", y="Cost", data=df, palette="Blues_d")

plt.title("The Analysis expenses on Subject (IT Economics)", fontsize=14)
plt.xlabel("Tool", fontsize=12)
plt.ylabel("Cost", fontsize=12)

plt.show()