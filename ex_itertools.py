from itertools import zip_longest


#zip_longest(): to retain the values in uneven list
x = [1, 2, 3]
y = [4,5,6]
z = [10,30,50,70]


newZipList = list(zip(x,y,z))
print("zip: {}".format(newZipList) )
#zip: [(1, 4, 10), (2, 5, 30), (3, 6, 50)]


newLongList = list(zip_longest(x,y,z))
print("zip_longest: {}".format(newLongList) )
#Returns: [(1, 4, 10), (2, 5, 30), (3, 6, 50), (None, None, 70)]
