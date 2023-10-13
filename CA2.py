import numpy as np
def compare_arrays(array1, array2):
  result = np.zeros(len(array1), dtype=bool)
  for i in range(len(array1)):
    result[i] = not np.isin(array1[i], array2)
  return result
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])
result = compare_arrays(array1, array2)
print(result)
