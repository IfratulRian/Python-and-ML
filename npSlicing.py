import numpy as np

arr1 = np.array([[1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5]])

arr1[1]*=2
arr1[2]*=3
arr1[3]*=4

#array[start : end : step]
print(arr1[0:])
