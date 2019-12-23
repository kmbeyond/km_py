d = {'x': 1, 'y': 2, 'z': 3}

print("------for loop by keys")
for k in d:
    print(k, '--->', d[k])

'''
x ---> {'x': 1, 'z': 3, 'y': 2}
z ---> {'x': 1, 'z': 3, 'y': 2}
y ---> {'x': 1, 'z': 3, 'y': 2}
'''


print("------items(): reads key & val as tuple")
for k in d.items():
    print(k)
'''
('z', 3) ---> {'z': 3, 'y': 2, 'x': 1}
('y', 2) ---> {'z': 3, 'y': 2, 'x': 1}
('x', 1) ---> {'z': 3, 'y': 2, 'x': 1}
'''

print("------items (read key & value) ")
for k, v in d.items():
    print(k, '--->', v)
'''
x ---> 1
y ---> 2
z ---> 3
'''



'''
print("------iteritems()")
#This is deprecated in Python3 & replaced by items() 
for k in d.iteritems():
    print (k, '--->', d)

'''
