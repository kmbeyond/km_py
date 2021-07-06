


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
