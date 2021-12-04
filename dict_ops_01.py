
#get counts of each items from list into dict
list_items = [1,4,6,5,2,9,1,5,8,3,2,5,1,7,2,9,2,3,5]

itm_counts = {}

# 1:using Collections.Counter
from collections import Counter
itm_counter = Counter(list_items)
itm_counts = dict(itm_counter)
#OR
#itm_counts = {k:v for k,v in itm_counter.items()}

# 2:manual loop
#for itm in list_items: itm_counts[itm] = itm_counts.get(itm, 0) + 1
#OR
#for itm in list_items: itm_counts[itm] = itm_counts[itm]+1 if itm in itm_counts else 1


print(itm_counts)