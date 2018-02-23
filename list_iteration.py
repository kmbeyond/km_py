



lst = [1, 2 , 6, 1, 4, 3]

print("----- List: read value")
for i in lst:
    print(i)

print("----- List: using index")
for i in range(len(lst)):
    print("{} - {}".format(i, lst[i]))




print("------ set: ordered & unique")
lstSet = set(lst)

for i in lstSet:
    print(i)

#NOTE: lstSet[0] gives TypeError: 'set' object does not support indexing

