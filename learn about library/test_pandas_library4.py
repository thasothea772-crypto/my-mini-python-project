# test pandas library part 4
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Tools": [
        "Cloud Server",
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
    "Cost": [2000, 2400, 3500, 5000]
}

df = pd.DataFrame(data)

print(df)

total_cost = df["Cost"].sum()
print(f"Total Cost: ${total_cost}")
avg_cost = df["Cost"].mean()
print(f"Average Cost: ${avg_cost}")
annual_cost = total_cost * 12
print(f"Annual Cost: ${annual_cost}")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x="Tools", y="Cost", data=df, palette="Blues_d")

plt.title("The Analysis expenses on Subject (IT Economics)", fontsize=14)
plt.xlabel("Tools", fontsize=12)
plt.ylabel("Cost", fontsize=12)

plt.show()