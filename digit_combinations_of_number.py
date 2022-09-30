
mynum=427
mylist = list(str(mynum))

print(f"input: {mylist}")

print("----itertools-----")
import itertools

print("itertools.combinations()")
print("-- 2 digits")
comb_list = list(itertools.combinations(mylist, 2))
comb_list2 = [i for i in comb_list if i[0]!=i[1]]
print(comb_list2)
print(sorted([int(''.join([str(i) for i in list(i)])) for i in comb_list2]))

print("-- 3 digits")
comb_list = list(itertools.combinations(mylist, 3))
comb_list3 = [i for i in comb_list if i[0]!=i[1] and i[2]!=i[1] and i[2]!=i[0]]
print(comb_list3)
print(sorted([int(''.join([str(i) for i in list(i)])) for i in comb_list3]))


print("itertools.product()")
print("-- 2 digits")
comb_list = list(itertools.product(mylist, repeat=2))
comb_list2 = [i for i in comb_list if i[0]!=i[1]]
print(comb_list2)
print(sorted([int(''.join([str(i) for i in list(i)])) for i in comb_list2]))

print("-- 3 digits")
comb_list = list(itertools.product(mylist, repeat=3))
comb_list3 = [i for i in comb_list if i[0]!=i[1] and i[2]!=i[1] and i[2]!=i[0]]
print(comb_list3)
print(sorted([int(''.join([str(i) for i in list(i)])) for i in comb_list3]))



#----manually
print("manual")


print("2 digit combinations:")

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

print("manual")
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


#-------
