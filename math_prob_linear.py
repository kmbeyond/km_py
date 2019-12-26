

#At a fair, admission fee for child=1.50, adult=4.00
#On a day, there are 2200 people entered, collected $5050
#How many children & adults?

#Sol:
#x1=num of children
#x2=num of adults
#x1+x2=2200
#x1*1.5+x2*4.00=5050

import numpy as np
A = np.array([[1,1], [1.5,4.0]])
b = np.array([2200, 5050])
print(np.linalg.solve(A, b))
