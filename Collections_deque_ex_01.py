

from collections import deque
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())
print("-----------")

d = deque(['ghi'])                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())

print("-----------")

d = deque(["cat", "rat", "tiger", "dog"])

for elem in d:                   # iterate over the deque's elements
    print(elem.upper())

print("----- append goat")
d.append("goat")
d.appendleft("lama")

for elem in d:                   # iterate over the deque's elements
    print(elem.upper())

print("----- add multiple elements")
d.extend(["hen", "turkey"])

for elem in d:                   # iterate over the deque's elements
    print(elem.upper())



print("----- pop")
d.pop()
d.popleft()

for elem in d:                   # iterate over the deque's elements
    print(elem.upper())


#empty deque
d.clear()


