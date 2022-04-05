import numpy as np

working_array = np.arange(0, 21, 1)
working_array = working_array**3
working_array[working_array > 10] = 0
value = working_array.sum()

print(f"Pole: {working_array}, Celková hodnota pole: {value}")



