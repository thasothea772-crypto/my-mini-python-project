# test numpy part 1
import numpy as np

monthly_cost = np.array([1500, 2000, 2500, 3000])

total_cost = np.sum(monthly_cost)

avg_cost = np.mean(monthly_cost)

print(f"The total cost: {total_cost}")
print(f"The average cost: {avg_cost}")