

#------swap any 2 digits in a number & check if any number falls between range

mynum=427
#all swap combinations: [247, 742, 724]
# check_in_limits_after_swap(427, 700,800)   => True because swap can give 724,742 that satisfy 700 > x > 800
# check_in_limits_after_swap(427, 900,1000)  => False because none of numbers after swapping can satisfy 900 > x > 1000

#mystr=str(mynum)

#swap using list
def swap_digits(mynum):
    mylist = list(str(mynum))
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            #yield (i,j)
            mylist_temp=mylist.copy()  #mylist_temp=mylist[:]
            #swap elements
            mylist_temp[i],mylist_temp[j] = mylist_temp[j], mylist_temp[i]
            #temp=mylist_temp[i]
            #mylist_temp[i]=mylist_temp[j]
            #mylist_temp[j]=temp
            print(f"{mylist}: {i}-{j} => {mylist_temp}")
            yield int("".join(mylist_temp))

print(list(swap_digits(mynum)))
#=> 
#['4', '2', '7']: 0-1 => ['2', '4', '7']
#['4', '2', '7']: 0-2 => ['7', '2', '4']
#['4', '2', '7']: 1-2 => ['4', '7', '2']
#[247, 724, 472]

#OR swap using bytearray
def swap_digits_using_bytes(mynum):
    myba = bytearray(str(mynum).encode())
    for i in range(len(myba)-1):
        for j in range(i+1,len(myba)):
            myba_temp=myba.copy()  #myba_temp=myba[:]
            #swap elements
            myba_temp[i],myba_temp[j]=myba_temp[j],myba_temp[i]
            #temp=myba_temp[i]
            #myba_temp[i]=myba_temp[j]
            #myba_temp[j]=temp
            print(f"{myba.decode()}: {i}-{j} => {myba_temp.decode()}")
            yield int(myba_temp.decode())

print(list(swap_digits_using_bytes(mynum)))
#=>
#427: 0-1 => 247
#427: 0-2 => 724
#427: 1-2 => 472
#[247, 724, 472]


def check_in_limits_after_swap(num_to_check, min1, max1):
    all_matches = list(swap_digits_using_bytes(num_to_check))
    for i in all_matches:
        if i>min1 and i<max1:
            return True
    return False


print ( check_in_limits_after_swap(427, 700,800) )
print ( check_in_limits_after_swap(427, 900,1000) )



#-----Solution with minimal code

#return copy of swapped list (DONT SWAP IN ORIGINAL LIST)
def my_swap(mylist, i ,j):
 mylist_temp=mylist.copy()
 mylist_temp[i],mylist_temp[j] = mylist_temp[j], mylist_temp[i]
 return mylist_temp

#get swapped numbers list
def get_swapped_nums_list(mynum):
    mylist = list(str(mynum))
    return [int("".join(my_swap(mylist,i,j))) for i in range(len(mylist)-1) for j in range(i+1,len(mylist)) ]

def check_in_limits_after_swap(num_to_check, min1, max1):
    all_matches = list(get_swapped_nums_list(num_to_check))
    for i in all_matches:
        if i>min1 and i<max1:
            return True
    return False

check_in_limits_after_swap(427, 700,800)
check_in_limits_after_swap(427, 900,1000)

#------------


