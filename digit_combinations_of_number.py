
mynum=427
mylist = list(str(mynum))

#-----2 digits
print("2 digit combinations:")

import itertools
combination_list = list(itertools.product(mylist,repeat=2))
print(sorted([int(''.join([str(i) for i in list(i)])) for i in combination_list]))
#=>gives duplications like 44,22,77

#----manually
def combinations_2(s):
    new_list=[]
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            new_list.append((s[i], s[j]))
            new_list.append((s[j], s[i]))
    return new_list

combination_list = list(combinations_2(mylist))

print(sorted([int(''.join([str(i) for i in list(i)])) for i in combination_list]))


#-----3 digits
print("3 digit combinations:")

import itertools
combination_list = list(itertools.product(mylist,repeat=3))
print(sorted([int(''.join([str(i) for i in list(i)])) for i in combination_list]))
#=>gives duplications like 444, 442, 422,...

#----manual
def combinations_3(s):
    new_list=[]
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                new_list.append((s[i], s[j], s[k]))
                new_list.append((s[i], s[k], s[j]))
                new_list.append((s[j], s[k], s[i]))
                new_list.append((s[j], s[i], s[k]))
                new_list.append((s[k], s[i], s[j]))
                new_list.append((s[k], s[j], s[i]))
    return new_list

combination_list = list(combinations_3(mylist))

print(sorted([int(''.join([str(i) for i in list(i)])) for i in combination_list]))
