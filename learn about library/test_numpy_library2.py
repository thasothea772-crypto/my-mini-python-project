# test numpy part 1
import numpy as np

def line():
    print("=====================================================================")

monthly_cost = np.array(
    [1600, 1200, 2000, 1500, 1900, 2500, 2300, 3000, 4000, 3500]
)
print()
line()
monthly_cost.sort()
print(f"The Monthly_cost: {monthly_cost}")

total_cost = np.sum(monthly_cost)
avg_cost = np.mean(monthly_cost)
print(f"The Total Cost: ${total_cost}")
print(f"The Average Cost: ${avg_cost}")

print(f"The Min of Expenses: ${monthly_cost.min()}")
print(f"The Max of Expenses: ${monthly_cost.max()}")
line()