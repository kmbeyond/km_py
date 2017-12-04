import numpy as np

#my_list1 = [1.22, 1.44, 1.55, 1.88, 1.33]
my_list1 = [2, 4, 8, 6, 10]

my_array1 = np.array(my_list1)

print("numpy array:" )
print(my_array1)
#[ 2  4  8  6 10]

my_array1
#array([ 2,  4,  8,  6, 10])

type(my_array1)
#<class 'numpy.ndarray'>

print("Val at 4: {}".format(my_array1[3])) #index starts from 0
print("Contents of Array")
>>> for i in my_array1: print("{}".format(i))

#Print index & value
for i in range(len(my_array1)):
    print("Index: {} has : {}".format(i, my_array1[i]))


print(my_array1[1:3]) #Elememts from idex 1 till 3 (3 is exclusive) => 1,2
#[ 1.44  1.55]

print("Assign values:")
for i in range(len(my_array1)):
    my_array1[i] = float("{}.{}{}".format(i,i,i))

for i in range(len(my_array1)):
    print("Index: {} has : {}".format(i, my_array1[i]))


print("2D array:")
my_list2 = [5,9, 7, 3, 11]

my_2dlist = [my_list1, my_list2]
my_2darray = np.array(my_2dlist)

print(my_2darray)
#[[ 2  4  8  6 10]
# [ 5  9  7  3 11]]

my_2darray
#array([[ 2,  4,  8,  6, 10],
#       [ 5,  9,  7,  3, 11]])

print("Array shape: {}".format(my_2darray.shape))
#Array shape: (2, 5)

print("Array type: {}".format(my_2darray.dtype))
#Array type: int64


print("Zeros array:")
my_zeros_array = np.zeros(5)
print("1D Zero Array shape: {}".format(my_zeros_array.shape))
#1D Zero Array shape: (5,)

print("2D Zero Array: ")
my_zeros_2d_array = np.zeros([5, 5])
print(my_zeros_2d_array)

print("2D array value at index(2,3);{}".format(my_zeros_2d_array[2,3]))
print("Identity array:")
my_identity_array=np.eye(5)
print(my_identity_array)

print("Evenly placed array:")
my_evenly_array = np.arange(0, 10)
print(my_evenly_array)
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Evenly placed array:")
my_odd_array = np.arange(1, 20, 2) #between 1 - 20 & step by 2
print(my_odd_array)
#array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])

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


#Universal Functions
numArray = np.arange(1,20)
print(np.sqrt(numArray))

#random numbers
print("Random numbers:")
randomArr1 = np.random.randn(10)
#OR np.random.random(10)
print(randomArr1)
print(np.add(randomArr1, 2))

#print(np.maximum(randomArr1))



#where()
A = np.array([1,2,3,4])
B = np.array([100,200,300,400])
condition = np.array([True, True,False,False])
answer = np.where(condition, A, B)
#Returns Array()
#array([  1,   2, 300, 400])

#using list comprehensions
answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]
#Returns: List
#[1, 2, 300, 400]

np.where(A<3,0,A)
#Returns: array([0, 0, 3, 4])

numArr = np.array([3,8,2,4,8])
np.unique(numArr)

np.sort(numArr)


#randn() returns an array of random numbers
#arr=randn(5,5)



arr = np.array([1,2,3])

print(arr.sum())

print(arr.sum(0))

#mean
print(arr.mean())

print(arr.std())

#variance
print(arr.var())
my_array1 = np.array([2, 4, 8, 6, 10])
np.diag(my_array1)
#array([[ 2,  0,  0,  0,  0],
#       [ 0,  4,  0,  0,  0],
#       [ 0,  0,  8,  0,  0],
#       [ 0,  0,  0,  6,  0],
#       [ 0,  0,  0,  0, 10]])


bool_arr =np.array([True,False,True])

print(bool_arr.any())

print(bool_arr.all())

###Operations on numpy arrays
my_array1 = np.array([2, 4, 8, 6, 10])

my_array2 = np.array([5,9, 7, 3])

#Arrays must be of same size for arithmetic operations
my_array1+my_array2
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: operands could not be broadcast together with shapes (5,) (4,)

#Product
#Outer product
np.outer(my_array1, my_array2)
#array([[10, 18, 14,  6],
#       [20, 36, 28, 12],
#       [40, 72, 56, 24],
#       [30, 54, 42, 18],
#       [50, 90, 70, 30]])

#inner product
np.inner(my_array1, my_array2)
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#ValueError: shapes (5,) and (4,) not aligned: 5 (dim 0) != 4 (dim 0)

#Append an element to make it same length
my_array2 = np.append(my_array2, [11])
np.inner(my_array1, my_array2)
#=> 230

#This is output as:
my_array1.dot(my_array2)

#File handling using np
print("numpy file handling:")
numArr = np.array([3,8,2,4,8])

np.save('myarray.txt', numArr)


np.load('myarray.txt.npy')
