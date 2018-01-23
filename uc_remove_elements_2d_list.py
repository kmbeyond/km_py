
'''
Program to read a 2D list,
    iterate the list,
    create new list with records if the value at index 2 is greater than 10

Input:
    -
Output:
    -

Author: Kiran Miryala/7897655

Steps:


Execution:
python uc_remove_elements_2d_list.py
'''

import sys

#Delete from a 2D list
itemList = [["Jason","Carl", 4],["Kim","Jane", 8], ["Kevin","James", 13],["Roul","Adams", 17], ["Paul","Ryan", 9]]

print("Full 2D list: {}".format(itemList))
#name = input("Enter name: ")
name=10
print("Removing an element if data at index 2 > {}".format(name))

#---Method#1 (Optimized): using List Comprehension
#list = [rec for rec in itemList if rec[2] < 10]


#Method#2: usig iteration (for doesn't work)
i=0
while(i < len(itemList)):
    print(itemList[i])
    if(int(itemList[i][2]) > 10):
        itemList.pop(i)
        print("---deleted {}".format(i))
        i = i - 1
    i=i+1

#NOTE: NOT TO USE for loop because we can't decrement in for loop
#Ex: for i in range(len(itemList)) ):



#----Method#3: Get None for the matched rec & delete in next step
#newList = [itemList[i] if itemList[i][2] < 10 else None for i in range(len(itemList))]

#Remove None from the list
#remove(None) #This removes only 1 occurrence
#itemList = [value for value in newList if value != None]

print("New list: {}".format(itemList) )

del itemList