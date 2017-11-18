

dictEmp={"zzz":"zval", "fname":"John", "lname":"Jackson", "aaa":"aVal"}
print(dictEmp)

#Access Dictionary using Key
#Iterate through a dictionary
for key in dictEmp.keys():
    print (key , '=', dictEmp[key])

sWhere=""
for key in dictEmp.keys():
    sWhere= sWhere + key + '=' + dictEmp[key] + ' AND '
print("Full string: {}".format(sWhere[:-5]))

lstCols=set(dictEmp)
print(lstCols)

sWhere=""
for key in lstCols:
    sWhere= sWhere + key + '=' + dictEmp[key] + ' AND '
print("Full string: {}".format(sWhere[:-5]))
