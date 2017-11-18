import numpy as np

my_list1 = [1.22, 1.44, 1.55, 1.88, 1.33]

my_array1 = np.array(my_list1)

print("numpy array:" )
print(my_array1)

print(type(my_array1))

my_list2 = [2.33, 2.66, 2.22, 2.99, 2.77]

my_list = [my_list1, my_list2]

print("2D array:")
my_array = np.array(my_list)

print(my_array)

print("Array shape: {}".format(my_array.shape))
print("Array type: {}".format(my_array.dtype))


print("Zeros array:")
my_zeros_array = np.zeros(5)
print("1D Zero Array shape: {}".format(my_zeros_array.shape))

print("2D Zero Array: ")
my_zeros_2d_array = np.zeros([5, 5])
print(my_zeros_2d_array)

print("Identity array:")
my_identity_array=np.eye(5)
print(my_identity_array)

print("Evenly placed array:")
my_evenly_array = np.arange(0, 10)
print(my_evenly_array)

print("Evenly placed array:")
my_odd_array = np.arange(1, 20, 2) #between 1 - 20 & step by 2
print(my_odd_array)

#from 0-5 (5 is excluded)
print("first 5 elements")
print(my_evenly_array[:5])

print("Copy of reference (any changes to copy would affect the original array):")
my_array = np.arange(0, 20)
print(my_array)

my_array_ref_copy = my_array
my_array_ref_copy[:] = 5
print("Original array:")
print(my_array)

print("Use copy() method to make a copy:")
my_array = np.arange(0, 20)
print(my_array)
my_array_ref_copy2 = my_array.copy()
my_array_ref_copy2[:] = 5
print("Original array:")
print(my_array)

