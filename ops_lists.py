
listNum=[11, 22, 33,44,55,66,77,88,99]
print(listNum)

listStrings = ['aaaa',"bbbb",'aaaa',"cccc"]
print(listStrings)


#Create list using range() (use xrange() in Python 2)
listNum=list(range(10)) #10 is excluded
print(listNum)
#=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

listNum=list(range(3, 10)) #from 3 to 10 (10 is excluded)
print("list from 3-10: {}".format(listNum) )
#=> [3, 4, 5, 6, 7, 8, 9]




#------------------Iterate or Loop through list-----------------
print("Iterate manually.....")
for item in listStrings:
    print(item)

#iterate using index
for i in range(len(listStrings)):
    print("listStrings[{}] has {}".format(str(i), listStrings[i]))



#---------------List slicing---------
listNum=list(range(3, 20))
outputList = listNum[:4]
print(outputList) #Slice of list from start to index 2(exclusive)
#=> [3, 4, 5, 6]

outputList=listNum[1:4]
print(outputList) #Slice of list from index 1 to 4(exclusive)
#=>[4, 5, 6]

#Last 2
#NOTE: Because the indexing in reverse starts with -1
outputList = listNum[-2:]
print(outputList)
#=> prints last 2 list items
#=>[18, 19]

#List from starting index & step by 2
outputList = listNum[1::2]
print(outputList )
#=> [4, 6, 8, 10, 12, 14, 16, 18]

#listNum[:] = 99
print(listNum)





print("#--------------------Operations on list--------------")
#Append items to list: use append() function
listNum=[22, 44, 11]
print("Original list {}".format(listNum))

listNum.append(33)
print("After appending 33: {}".format(listNum) )
#[22, 44, 11, 33]

listNum.append([88, 99]) #List is added as ONE element
print("After appending a List: {}".format(listNum) )

#insert element at an index
listNum.insert(3, 55)
print("After inserting 55 @ index=3: {}".format(listNum) )
#[55, 22, 44, 11, 33]


#Delete an element from list; This removes ONLY one occurrence
listNum.remove(55)
print("After removing 55: {}".format(listNum) )
#=> [22, 44, 11, 33]

#delete top element: use pop() function
listNum.pop()
print("After popping: {}".format(listNum))
#=> [22, 44, 11]

listNum.pop(1) #remove element at index 1
print("After popping element at index 1: {}".format(listNum))
#=> [22, 11]

print("Sorting list:")
lst=[2,9,4,6,1]
for i in sorted(lst): print(i)

for i in reversed(lst): print(i)

#Create list using list() & range()
listRange=list(range(10, 25))
print("create list from 10 - 25: {}".format(listRange) )
#=> [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

##This creates list using every 2nd in range
listRange=list(range(5, 16, 2))
print("create list from 5 - 16 step by 2: {}".format(listRange) )
#=> [5, 7, 9, 11, 13, 15]


#----- Search in a list -----
iSearchNum=33
if(iSearchNum in listNum):
    print( str(iSearchNum)+" is found")
else:
    print(str(iSearchNum)+" NOT FOUND")


#----- search for a string in a list of strings -----
#lst_columns = spark.table("kmdb.table").columns
lst_columns = ["mid", "name", "chain_code", "address"]

any("chain" in str for str in lst_columns)
=> True

#Generate new list of matches using List Comprehension
[str for str in lst_columns if "chain" in str]
=> ['chain_code']


#Scenario: insert values dynamically
#loop list using while
'''
i=1
while i < len(AllWords):
    print("{} = {}".format(i, AllWords[i]))
    if(i%3==0):
        AllWords.insert(i, '\n')
        print("New Line added.")
    i+=2
'''

#---------------------------------
#Scenario: Break the list into equal chunks
inputList= list(range(35))
numItems=10


#Using List Comprehension

outputList = [ inputList[i : i+numItems] for i in range(0, len(inputList), numItems)]

for i in range(len(outputList)):
    print("outputList[{}] = {}".format(str(i), outputList[i]))

#import numpy as np
#outputList = np.array_split(inputList, numItems)

#Using a method
def chunks(l, n):
    for i in range(0, len(l), numItems):
        yield l[i : i+numItems]


outputList = list(chunks(inputList, numItems))

for i in range(len(outputList)):
    print("outputList[{}] = {}".format(str(i), outputList[i]))


#merge successive elements
inputListStr=list(map(str, inputList)) #Converting to string/char

outputList = ['+'.join( inputListStr[i : i+numItems]) for i in range(0, len(inputListStr), numItems)]
print("Full list: {}".format( outputList) )
for i in range(len(outputList)):
    print("outputList[{}] = {}".format(str(i), outputList[i]))

print("#--------------------------------2D/Multi-D Lists------------------")
#2D list:
tokenCountList = [['a', '7'], ['b', '3'], ['c', '4'], ['d', '6'], ['e', '8'], ['f', '1']]

for i in range(len(tokenCountList)):
    print("{}: {} -> {}".format(i, tokenCountList[i][0], tokenCountList[i][1] ) )

#MUlti-D list:
print("Multi Dim list:")
multiDList = [['a', ['1','7']], ['b', ['2','3']], ['c', ['3','4']], ['d', ['4','6']], ['e', ['5','8']], ['f', ['6','1']] ]

for i in range(len(multiDList)):
    print("{}: {} -> {} -> {}".format(i, multiDList[i][0], multiDList[i][1], multiDList[i][1][0] ) )


#List of tuples
print("List of tuples:")
tokenCountList = [('a', 7), ('b', 3), ('c', 4), ('d', 6), ('e', 8), ('f', 1)]

for key in tokenCountList:
    print("tuple @ 0 = '{}' , 1 = {}".format(key[0] , key[1]))

#Extract elements at index 1 of 2D into 1D list
newList = []
for val in tokenCountList: newList.append(val[1])

print(newList)
tokenCountList[:][1]

#-----iterate using itertools functions
#zip(): Returns an iterator of tuples for each element in (one or more) lists simultaneosly
#truncates to the smallest list; use zip_longest() to retain till longest list

x = [1, 2, 4,5,8,9]
y = [100,300,400,700]
zipped = zip(x,y)
#zippedList = list( zip(x, y) ) #in Python 3.6
zippedList = [(x,y) for x,y in zipped]
print("new zipped list: {}".format(zippedList))
#returns: [(1, 100), (2, 300), (4, 400), (5, 700)]


#zip multiple lists
z = [10,30,50,70]
zipped2 = zip(x,y,z)
#list(zipped)
#=> [(1, 4, 10), (2, 5, 30), (3, 6, 50)]

#zip_longest(): to retain the values in uneven list
from itertools import zip_longest
#zippedList = list(zip_longest(x,y,z)) #in Python 3.6
zippedList = [(x,y,z) for x,y,z in zip_longest(x,y,z)]
print("new zipped list: {}".format(zippedList))


#add values at same index from 2 lists
ListA = [1,2,3,4,5]
ListB = [10,20,30,40,50,60,70]

[x + y for x, y in zip(ListA, ListB)]
#=>[11, 22, 33, 44, 55]

#Add while retaining values from longer list
[x + y for x, y in zip_longest(ListA, ListB, fillvalue=0)]
#=> [11, 22, 33, 44, 55, 60, 70]


#Break list of tuples into separate lists
x2, y2 = zip(*zip(x, y))
#x == list(x2) and y == list(y2) #not working in 3.5

x1, x2, x3 = zip(*zippedList)
print("unzipped x={}; y={}".format(x1,x2))



#-------------------

