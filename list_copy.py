


def print_list(lst):
    print("Printing list: {}".format(len(lst)))
    for l in range(len(listNum)):
        print("args {}: {}".format(l, lst[l]))

listNum=[11, 22, 33,44, 55, 66, 77, 88, 99]

listNum=[[1.2,1.5,1.7],[2.4,2.7,2.8],[3.5,3.2,3.7],[5.3,5.2,5.5]]
print_list(listNum)

#NOTE: This operator gives a new reference to original list
listNum2 = listNum

#Create a copy to eliminate other object change data
#multiple ways to make copies
listNum3=listNum[:]
listNum4=listNum.copy()
listNum5=list(listNum)
import copy
listNum6=copy.copy(listNum) #slower because this has to find out the type of list elements
listNum7=copy.deepcopy(listNum)


print("listNum2: {}".format(listNum2) )
print("listNum3: {}".format(listNum3) )
print("listNum4: {}".format(listNum4) )
print("listNum5: {}".format(listNum5) )
print("listNum6: {}".format(listNum6) )
print("listNum7: {}".format(listNum7) )


print("Popping an element from listNum: {}".format(listNum) )
listNum.pop()

print("listNum2: {}".format(listNum2) )
print("listNum3: {}".format(listNum3) )
print("listNum4: {}".format(listNum4) )
print("listNum5: {}".format(listNum5) )
print("listNum6: {}".format(listNum6) )
print("listNum7: {}".format(listNum7) )
