# test numpy part 4: Array(Reshaping)
import numpy as np

a = np.arange(6)
print(f"Array: {a}")

b = a.reshape(2, 3)
print(f"After array is reshaped: \n{b}")