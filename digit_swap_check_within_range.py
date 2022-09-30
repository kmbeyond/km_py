

#------swap any 2 digits in a number & check if any number falls between a limit
# check_in_limits_after_swap(427, 700,800)   => True because swap can give 724,742 that falls within 700 & 800
# check_in_limits_after_swap(427, 900,1000)  => none of numbers after swapping can fall within 700 & 800


mynum=427
#mystr=str(mynum)

#swap using list
def swap_digits(mynum):
    mylist = list(str(mynum))
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            if i!=j:
                #yield (i,j)
                temp=mylist[i]
                mylist[i]=mylist[j]
                mylist[j]=temp
                yield int("".join(mylist))


print(list(swap_digits(mynum)))
#=> ['247', '742', '472', '427', '724', '742']

#OR swap using bytearray
def swap_digits_using_bytes(mynum):
    mybc = bytearray(str(mynum).encode())
    for i in range(len(mybc)):
        for j in range(len(mybc)):
            if i!=j:
                temp=mybc[i]
                mybc[i]=mybc[j]
                mybc[j]=temp
                yield int(mybc.decode())


print(list(swap_digits_using_bytes(mynum)))
#=> ['247', '742', '472', '427', '724', '742']



def check_in_limits_after_swap(num_to_check, min1, max1):
    all_matches = list(swap_digits_using_bytes(num_to_check))
    for i in all_matches:
        if i>min1 and i<max1:
            return True
    return False


print ( check_in_limits_after_swap(427, 700,800) )
print ( check_in_limits_after_swap(427, 900,1000) )




