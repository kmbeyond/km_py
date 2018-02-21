

d = {'x': 1, 'y': 2, 'z': 3}

print("------for loop by keys")
for k in d:
    print(k, '--->', d[k])

'''
x ---> {'x': 1, 'z': 3, 'y': 2}
z ---> {'x': 1, 'z': 3, 'y': 2}
y ---> {'x': 1, 'z': 3, 'y': 2}
'''


print("------items")
for k in d.items():
    print(k, '--->', d)
'''
('z', 3) ---> {'z': 3, 'y': 2, 'x': 1}
('y', 2) ---> {'z': 3, 'y': 2, 'x': 1}
('x', 1) ---> {'z': 3, 'y': 2, 'x': 1}
'''


'''
print("------iteritems")
for k in d.iteritems():
    print (k, '--->', d)

'''

