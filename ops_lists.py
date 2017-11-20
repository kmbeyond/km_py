
listNum=[11, 22, 33,44,55,66,77,88,99]
print(listNum)


print(listNum[:2]) #Slice of list from start to index 2(exclusive)


print(listNum[1:4]) #Slice of list from index 1 to 4(exclusive)


#Last 2
#NOTE: Because the count in reverse starts with -1.
print(listNum[-2:])


listStrings = ['aaaa',"bbbb",'aaaa',"cccc"]
print(listStrings)

#Iterate or Loop through list
for k in listStrings:
    print(k)

#iterate list
for i in range(len(listStrings)):
    print(i)

#iterate using index
for i in range(len(listStrings)):
    print(str(i) + " has " + listStrings[i])



#Operations on list
#Append items to list: use append() function
listNum=[22, 44, 11]
listNum.append(33)
print(listNum)


#Delete a top element: use pop() function
listNum.pop()
print(listNum)


#Create list using list() & range()
listRange=list(range(20, 25))
print(listRange)


##This creates list using every 2nd in range
listRange=list(range(20, 25, 2))
print(listRange)



#Search in a list
iSearchNum=33
if(iSearchNum in listNum):
    print( str(iSearchNum)+" is found")
else:
    print(str(iSearchNum)+" NOT FOUND")

#2D list:
tokenCountList = [['a', '7'], ['b', '3'], ['c', '4'], ['d', '6'], ['e', '8'], ['f', '1']]

for i in range(len(tokenCountList)):
    print("{} -> {}".format( tokenCountList[i][0], tokenCountList[i][1] ) )

#MUlti-D list:
print("Multi Dim list:")
multiDList = [['a', ['1','7']], ['b', ['2','3']], ['c', ['3','4']], ['d', ['4','6']], ['e', ['5','8']], ['f', ['6','1']] ]

for i in range(len(multiDList)):
    print("{} -> {} -> {}".format( multiDList[i][0], multiDList[i][1], multiDList[i][1][0] ) )


#List of tuples
print("List of tuples:")
tokenCountList = [('a', 7), ('b', 3), ('c', 4), ('d', 6), ('e', 8), ('f', 1)]

for key in tokenCountList:
    print( key[0] , '-', key[1])

#Extract elements at index 1 of 2D into 1D list
newList = []
for val in tokenCountList: newList.append(val[1])

print(newList)
