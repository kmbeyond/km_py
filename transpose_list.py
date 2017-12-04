

#even array
aMyArray = [ ['a1', 'a2','a3'], ['b1','b2','b3'], ['c1','c2', 'c3']]
aMyArrayT = [[row[i] for row in aMyArray] for i in range(len(aMyArray))]
print(aMyArrayT)

#uneven & manual
aMyArray = [ ['a1', 'a2','a3'], ['b1','b2','b3','b4','b5'], ['c1','c2']]

aMyArrayTrsp = []
aMyArrayTemp = []

sRec = ""
iMaxRows = 0
iMaxCols = 0

print ("initial array:")
for i in range(len(aMyArray)):
    sRec = ""
    for j in range(len(aMyArray[i])):
        sRec = sRec+","+aMyArray[i][j]
    print (sRec)

print ("Finding max")
iMaxCols = len(aMyArray)
for i in range(len(aMyArray)):
    if(iMaxRows<len(aMyArray[i])):
        iMaxRows = len(aMyArray[i])
print("Max rows="+str(iMaxRows))
print("Max cols="+str(iMaxCols))

print ("Creating a blank 2D list..")
for i in range( iMaxRows ):
    aMyArrayTemp = []
    for j in range(iMaxCols ):
        aMyArrayTemp.append("")
    aMyArrayTrsp.append(aMyArrayTemp)

print ("transposing..")
for i in range( iMaxRows ):
    for j in range(iMaxCols):
        try:
            aMyArrayTrsp[i][j]=aMyArray[j][i]
        except IndexError:
            aMyArrayTrsp[i][j]=""

print ("Final output:")
print(aMyArrayTrsp)
for i in range(len(aMyArrayTrsp)):
    sRec = ""
    for j in range(len(aMyArrayTrsp[i])):
        sRec = sRec+","+aMyArrayTrsp[i][j]
    print (sRec)
