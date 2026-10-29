import pandas as pd

data = {
    "Year": [2023, 2024, 2025, 2026],
    "Cloud Cost": [1500, 2000, 2500, 3000],
    "Server Maintenance": [2500, 3000, 3500, 4000],
}

df = pd.DataFrame(data)

df["Total Cost"] = df["Cloud Cost"] + df["Server Maintenance"]

df["Avg Cost"] = df["Total Cost"]/4
print()
print("========================= Whole Data =========================")
print(df)

print()
high_servermaintenance_cost = df[df["Server Maintenance"] > 3999]
print("=================== The highest expenditure ==================")
print(high_servermaintenance_cost)