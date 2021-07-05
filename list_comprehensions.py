
lst = [ 3, 5, 9]
#Get sqrsList list

#Method#1: usual way
sqrsList = []
for x in lst:
    sqrsList.append(x**2)

for v in sqrsList: print(v)

#Method#2: map()
sqrsList = list(map(lambda x: x**2, lst))
print(sqrsList)


#Method#3: list comprehensions *****

sqrsList = [x**2 for x in lst]
print(sqrsList)


import numpy as np

A = np.array([1,2,3,4])

B = np.array([100,200,300,400])

condition = np.array([True, True,False,False])

answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]
print(answer)
