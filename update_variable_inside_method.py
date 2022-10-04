


#------updates inside method

#----- update string => Local, NOT reflect outside
mystr='abcd'

def update_string(mystr):
    mystr="x"+mystr

update_string(mystr)
print(mystr)
#=> abcd

update_string(mystr)
print(mystr)
#=> abcd


#----update list => original object changes, reflect outside
mylist1=[1,2,3,4]

def pop_and_print(mylist):
    mylist.pop(0)

pop_and_print(mylist1)
print(mylist1)
#=> [2, 3, 4]

pop_and_print(mylist1)
print(mylist1)
#=> [3, 4]



#------update bytestring => NOT reflect outside

mybytestring = "abcd".encode()

def update_bytearray(mybastr):
    mybastr=("x"+mybastr.decode()).encode()

update_bytearray(mybytestring)
print(mybytestring.decode())
#=> abcd

update_bytearray(mybytestring)
print(mybytestring.decode())
#=> abcd



