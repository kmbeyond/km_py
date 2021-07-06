d = {'x': 1, 'y': 2, 'z': 3}

print("------for loop by keys")
for k in d:
    print(k, '--->', d[k])


print("------items(): reads key & val as tuple")
for k in d.items():
    print(k, ' --> ', k[0], ' -- ', k[1])

print("------items (read key & value) ")
for k, v in d.items():
    print(k, '--->', v)

print("------by keys ")
for k in d.keys():
    print(k, '--->', d[k])

#for k in sorted(d.keys()):
#    print(k, '--->', d[k])


print("------by values ")
for v in d.values():
    print(v)


