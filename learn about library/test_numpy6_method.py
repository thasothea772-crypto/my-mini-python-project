# test numpy part 6: method sort and unique
import numpy as np

data1 = np.array([10, 20, 20, 30, 10, 15, 15, 40, 50, 30, 40, 50])

print(data1)
print()
data1.sort()
print(data1)

print()
print(np.unique(data1))