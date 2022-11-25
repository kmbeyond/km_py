 
import random

list_data=[]
list_lookup = range(1000)
loop_times=1000

def gen_random_from_list(list_lookup):
    return list_lookup[random.randint(0, len(list_lookup) - 1)]

def gen_random_from_list2(list_lookup, already_picked_list, trials=3):
    # Does not return duplicates
    while trials > 0:
        rand_item = random.randint(0, len(list_lookup) - 1)
        if rand_item in already_picked_list:
            trials -= 1
        else:
            #already_picked_list.append(rand_item)
            return rand_item
    return ""



time_start = datetime.now()
for i in range(loop_times):
    get_next_item = gen_random_from_list2(list_lookup, list_data, 3)
    if get_next_item!='': list_data.append(get_next_item)

time_end = datetime.now()

time_diff = time_end-time_start

time_diff


print(len(list_data))

