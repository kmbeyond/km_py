


my_list=[11,22,44,33,66,88,99]
print("--- List iteration ---")
for i in my_list:
    print(i)

print("--- Print from item#2 ---")
print(my_list[2:])
print(my_list[2:5])
print("--- Print last item ---")
print(my_list[-1:])

print("--- Print even numbers from List ---")

#using list comprehension
print([x for x in my_list if x%2==0])

#using filter & lambda
print(list(filter(lambda x: x%2==0, my_list)))

#using filter() & function
def not_even(x):
    return x if x%2==0 else None

print(list(filter(not_even, my_list)))

#append: add items to list
my_list.append(110)
print(my_list)

#extend: merge 2 lists into one
my_list.extend([112])
print(my_list)

#-------------------------2Dimensional lists (List of Lists)
array_2d = [
    [1,0,1],
    [1,1,1],
    [0,0,1]
]

def print_2darray(array_2d):
    for i in range(len(array_2d)):
        for j in range(len(array_2d[i])):
            print(f"({i},{j}) = {array_2d[i][j]}")

print_2darray(array_2d)
(0,0) = 1
(0,1) = 0
(0,2) = 1
(1,0) = 1
(1,1) = 1
(1,2) = 1
(2,0) = 0
(2,1) = 0
(2,2) = 1

-----------

list_of_lists=[[]]

list_of_lists[0].extend([1,2])
print(f"{list_of_lists}")
list_of_lists.append([5,7])
print(f"{list_of_lists}")

