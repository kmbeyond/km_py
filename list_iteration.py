


lst = [1, 2 , 6, 1, 4, 3, 6]

print("----- List: read value")
for i in lst:
    print(i)

print("----- List: using index")
for i in range(len(lst)):
    print("{} - {}".format(i, lst[i]))

print("List using List comprehension: ", [lst[i] for i in range(len(lst)) ])
print("Print using slicing: ", lst[0:len(lst)])

print("Reverse List using List comprehension: ", [lst[i] for i in range(len(lst)-1,-1,-1) ])
print("Reverse List using List slicing: ", lst[len(lst)-1:0:-1])

print("Sum=", sum(lst))
print("Max=", max(lst))

print("Number of highest items:", len([1 for i in lst if i==max(lst)]))


print("Percentage of count of each item in a list:")
lst2=[3, 5, 3, 2, 0,4,5,2,3,9]
itmSet=set(lst2)
for i in sorted(itmSet):
    itmCnt = len([1 for v in lst2 if v==i])
    print(i, " -> ", itmCnt*100/len(lst2))

print("--- using collections package...")
import collections
itmDict = collections.Counter(lst2)
for (itm, count) in itmDict.items():
    print("{} -> {}".format(itm, count*100/len(lst2)))


print("Percentage of each item in a list:")
lst2=[3, 5, 1, 7, 10]
for i in lst2:
    print(i, " -> ", i*100/sum(lst2))

print([i*100/sum(lst2) for i in lst2])


print("------ set: ordered & unique")
lstSet = set(lst)

for i in lstSet:
    print(i)

#NOTE: lstSet[0] gives TypeError: 'set' object does not support indexing

