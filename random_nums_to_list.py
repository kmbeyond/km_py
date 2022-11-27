

def gen_random_item_from_list(list_lookup):
    import random
    return list_lookup[random.randint(0, len(list_lookup) - 1)]

#overloaded function to check to get unique item
def gen_random_item_from_list2(list_lookup, add_to_list, retries):
    # Does not return duplicates
    while retries > 0:
        rand_item = gen_random_item_from_list(list_lookup)
        #print('random item:', rand_item)
        if rand_item in add_to_list:
            retries -= 1
        else:
            add_to_list.append(rand_item)
            break #works as return
            #return rand_item
    #return ""

def generate_random_num_list(loop_times, list_lookup, retries):
    list_data = []
    for i in range(loop_times):
        gen_random_item_from_list2(list_lookup, list_data, retries)
        #get_next_item = gen_random_item_from_list(list_lookup, list_data, retries)
        #if get_next_item!='': list_data.append(get_next_item)
    return list_data



list_lookup = list(range(1000))
loop_times = 100
retries = 1

from datetime import datetime

time_start = datetime.now()
my_list = generate_random_num_list(loop_times, list_lookup, retries)
time_end = datetime.now()
print("Items count:", len(my_list))

time_diff = time_end-time_start

time_diff

