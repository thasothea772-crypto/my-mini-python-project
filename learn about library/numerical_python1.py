import numpy as np

# Create the monthly expenses list in form of numpy array
monthly_cost = np.array([2000, 4000, 10000, 15000])

# Calculate the average cost
avg_cost = np.mean(monthly_cost) # mean for average

# Calculate the total cost
total_cost = np.sum(monthly_cost) # sum for total

# Show the result
print()
print(f"The Average cost: ${avg_cost}")
print(f"The Total Cost: ${total_cost}")
