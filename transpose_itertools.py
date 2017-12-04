import itertools


arr1 = [[1,2,3], [4,5], [], [6,7,8,9]]
print(arr1)

#Transpose into List
trsp1 = [list(tup) for tup in itertools.zip_longest(*arr1, fillvalue="")]
#NOTE: itertools.izip_longest() in Python2.x
#itertools.zip_longest() in Python3.x

print(trsp1)
#[[1, 4, '', 6], [2, 5, '', 7], [3, '', '', 8], ['', '', '', 9]]



#Transpose into tuples
trsp2 = list(itertools.zip_longest(*l, fillvalue=""))
print(trsp2)
#[(1, 4, '', 6), (2, 5, '', 7), (3, '', '', 8), ('', '', '', 9)]
