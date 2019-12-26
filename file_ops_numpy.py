import numpy as np

lst = []
#read file, convert data to float & append to list
for line in open("/home/kiran/km/km_big_data/data/data_2d.csv"):
#for line in open("C:\km\hadoop\data\data_2d.csv"):
    row = line.split(',')
    sample = list(map(float, row))
    lst.append(sample)

print(type(lst))


np_arr = np.array(lst)

print("shape=", np_arr.shape)

for line in np_arr:
    print(line)

for i in range(len(np_arr)):
    print("{} = {}".format(i, np_arr[i]))
