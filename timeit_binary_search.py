# importing the required modules
import timeit


# binary search function
def binary_search(mylist, find):
    while len(mylist) > 0:
        mid = (len(mylist)) // 2
        if mylist[mid] == find:
            return True
        elif mylist[mid] < find:
            mylist = mylist[:mid]
        else:
            mylist = mylist[mid + 1:]
    return False


# compute binary search time
def binary_time():
    SETUP_CODE = ''' 
from __main__ import binary_search 
from random import randint'''

    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
binary_search(mylist, find)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)

    # priniting minimum exec. time
    print('Binary search time: {}'.format(min(times)))


if __name__ == "__main__":
    binary_time()
