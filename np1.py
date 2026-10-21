import numpy as np

# print(np.__version__) 

arr = np.array([1,2,3,4])
arr*=2
# print(type(arr))
print(arr)

#2d array
arr1 = np.array([[1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5]])
print(arr1.ndim)

arr1[1]*=2
arr1[2]*=3
arr1[3]*=4

print(arr1)

arr2 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                 [[1,2,3],[4,5,6],[7,8,9]],
                 [[1,2,3],[4,5,6],[7,8,9]],
                 [[1,2,3],[4,5,6],[7,8,9]],
                 [[1,2,3],[4,5,6],[7,8,9]],
                 [[1,2,3],[4,5,6],[7,8,9]]])
print(arr2.ndim)
#print(arr2)
print(arr2[3,2,1])