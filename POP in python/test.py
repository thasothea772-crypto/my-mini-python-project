import numpy as np
from scipy import stats

data = [4, 7, 0, 7, 11, 4, 1, 15, 3, 5, 8, 7]

# Calculations
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode.mode[0]}")
print(f"Sorted Data: {sorted(data)}")