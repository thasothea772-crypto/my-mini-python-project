# test numpy part 3: indexing and slicing
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print()
print(matrix)
print()
print(f"Row line 0: {matrix[0]}")
print(f"Row line 1: {matrix[1]}")
print(f"Row line 2: {matrix[2]}")
print()
print(f"Value at [0, 0]: {matrix[0, 0]}") # Reault: 1
print(f"Value at [1, 2]: {matrix[1, 2]}") # Result: 6
print(f"Value at [2, 1]: {matrix[2, 1]}") # Result: 8
print()
print(f"Column 2: {matrix[:, 2]}") # Result: [3, 6, 9]
print(f"Column 0: {matrix[:, 0]}") # Result: [1, 4, 7]
print(f"Column 1: {matrix[:, 1]}") # Result: [2, 5, 8]