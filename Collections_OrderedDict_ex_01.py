
#Using OrderedDict
print("----- using OrdereDict: Maintains the order of entry")
import collections
d1 = collections.OrderedDict()
d1['d'] = 'D'
d1['e'] = 'E'
d1['b'] = 'B'
d1['c'] = 'C'
d1['a'] = 'A'
for k, v in d1.items():
    print(k, v)


print("----- using regular Dictionary: Order varies on every run")
d2 = {}
d2['d'] = 'D'
d2['b'] = 'B'
d2['c'] = 'C'
d2['e'] = 'E'
d2['a'] = 'A'
for k, v in d2.items():
    print(k, v)