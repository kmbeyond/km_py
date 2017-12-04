
listNum=[11, 22, 33,44,55,66,77,88,99]
print(listNum)


print(listNum[:2]) #Slice of list from start to index 2(exclusive)


print(listNum[1:4]) #Slice of list from index 1 to 4(exclusive)

#Last 2
#NOTE: Because the count in reverse starts with -1.
print(listNum[-2:])

#listNum[:] = 99
print(listNum)

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
#[22, 44, 11, 33]

#insert element at an index
listNum.insert(0, 55)
print(listNum)
#[55, 22, 44, 11, 33]

#Scenario: insert values dynamically
#loop list using while
i=1
while i < len(AllWords):
    print("{} = {}".format(i, AllWords[i]))
    if(i%3==0):
        AllWords.insert(i, '\n')
        print("New Line added.")
    i+=2



#Delete an element from list
listNum.remove(55)

#delete top element: use pop() function
listNum.pop()
print(listNum)

lst=[2,9,4,6,1]
for i in sorted(lst): print(i)

for i in reversed(lst): print(i)

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

#Delete from a 2D list
list = [["hello","son", 52],["welcome","home",65],["good","work",6]]
name = input("Name: ")
if name in list[]:
    del list[name]
    print("name + " deleted")
else:
    print("invalid name")


#List of tuples
print("List of tuples:")
tokenCountList = [('a', 7), ('b', 3), ('c', 4), ('d', 6), ('e', 8), ('f', 1)]

for key in tokenCountList:
    print( key[0] , '-', key[1])

#Extract elements at index 1 of 2D into 1D list
newList = []
for val in tokenCountList: newList.append(val[1])

print(newList)

#zip(): Returns an iterator of tuples for each element in (one or more) lists simultaneosly

x = [1, 2, 3]
y = [4,5,6]
zipped = zip(x, y)
list(zipped)
#returns: [(1, 4), (2, 5), (3, 6)]

z = [10,30,50,70]
zipped2 = zip(x,y,z)
list(zipped)
#returns: [(1, 4, 10), (2, 5, 30), (3, 6, 50)]

#zip_longest(): to retain the values in uneven list
from itertools import *
list(zip_longest(x,y,z))

x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)
