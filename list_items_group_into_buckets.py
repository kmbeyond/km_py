
#put items into bucket & get count in each bucket

items_list = [2,5,8,9,11,13,15,16,18,19,26]
bucket_size = 5

#Scenario#1: without given bucket boundaries

items_rounded = [int(i/bucket_size)*bucket_size for i in items_list]
#print(int(8/5)*5)
print(items_rounded)

items_grp_counts = {}
for i in items_rounded: items_grp_counts[i]=items_grp_counts.get(i,0)+1
#for i in items_rounded: items_grp_counts[str(i)+'-'+str(i+5)]=items_grp_counts.get(str(i)+'-'+str(i+5),0)+1

print(items_grp_counts)
#=> {0: 1, 5: 3, 10: 2, 15: 4, 25: 1}

items_bucket_counts = {}
items_bucket_counts = dict([(str(k)+'-'+str(k+bucket_size), v) for k,v in items_grp_counts.items()])
print(items_bucket_counts)
#=> {'0-5': 1, '5-10': 3, '10-15': 2, '15-20': 4, '25-30': 1}


#Scenario#2: with bucket boundaries, so put 0 in bucket if not existing
bucket_min = 1
#bucket_min = min(items_list)
bucket_max = 20
#bucket_max = max(items_list)

