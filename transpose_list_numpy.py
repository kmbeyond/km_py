#Transpose a 2D Array using numpy

import numpy as np

aMyArray = np.array([['a1', 'a2','a3'],
    ['b1','b2','b3','b4','b5', 'b6'], ['c1','c2']])
print(aMyArray)



'''
print ("initial array:")
for i in range(len(aMyArray)):
    sRec = ""
    for j in range(len(aMyArray[i])):
        sRec = sRec+","+aMyArray[i][j]
    print (sRec)
'''

aMyArrayTemp = np.array([])

sRec = ""
iMaxRows = 0
iMaxCols = 0



print ("Finding max")
iMaxCols = len(aMyArray)
for i in range(len(aMyArray)):
    if(iMaxRows<len(aMyArray[i])):
        iMaxRows = len(aMyArray[i])

print("Max rows="+str(iMaxRows))
print("Max cols="+str(iMaxCols))

print ("Creating a blank 2D array..")
aMyArrayTrsp = np.empty((iMaxRows, iMaxCols), dtype=object)

'''
#This is for List of Lists (if not using numpy)
for i in range( iMaxRows ):
    aMyArrayTemp = []
    for j in range(iMaxCols ):
        np.append(aMyArrayTemp,"")
    np.append(aMyArrayTrsp, aMyArrayTemp)
'''
print(aMyArrayTrsp)

print ("transposing..")
for i in range( iMaxRows ):
    for j in range(iMaxCols):
        try:
            aMyArrayTrsp[i][j]=aMyArray[j][i]
        except IndexError:
            aMyArrayTrsp[i,j]=""


print ("Final output:")
print(aMyArrayTrsp)


'''
for i in range(len(aMyArrayTrsp)):
    sRec = ""
    for j in range(len(aMyArrayTrsp[i])):
        sRec = sRec+","+aMyArrayTrsp[i][j]
    print (sRec)
'''
