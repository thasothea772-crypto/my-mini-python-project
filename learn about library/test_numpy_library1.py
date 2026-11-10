# test numpy part 1
import numpy as np
import pandas as pd

monthly_cost = np.array([1530, 1200, 1390, 2000, 1600, 1000, 2060, 3200, 2700, 4000])

monthly_cost.sort()
print(f"Data of monthly cost: {monthly_cost}")

total_cost = np.sum(monthly_cost)
avg_cost = np.mean(monthly_cost)
print(f"The total cost: ${total_cost}")
print(f"The average cost: ${avg_cost}")

print(f"The min of monthly cost: ${monthly_cost.min()}")
print(f"The max of monthly cost: ${monthly_cost.max()}")

df = pd.DataFrame(monthly_cost)
print(df)