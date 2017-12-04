
import numpy as np


#2D Matrices
l2D = [[1,2,3], [4,5,6], [7,8,9]]
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Convert a 2D List as numpy array
arr2D = np.array(l2D)
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])

arr2D[0]
#array([1, 2, 3])

print(arr2D[0,0])  #regular list: arr[0][0]
# 1

#NOTE: Can use numpy matrix() function
mtrx2D = np.matrix(l2D)

#matrix([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

#size of matrix
arr2D.shape


np.diag(arr2D)
#array([1, 5, 9])
#1D array returns 2D array
#2D array returns 1D array


#Sum of diag of matrix

np.trace(arr2D)
#15
np.diag(arr2D).sum()
#15
