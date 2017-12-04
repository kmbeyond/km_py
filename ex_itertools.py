from itertools import *


#zip_longest(): to retain the values in uneven list
x = [1, 2, 3]
y = [4,5,6]
z = [10,30,50,70]
list(zip_longest(x,y,z))
#Returns: [(1, 4, 10), (2, 5, 30), (3, 6, 50), (None, None, 70)]
