import numpy as np

X = []

#for line in open("/home/kiran/km/km_hadoop/data/data_2d.csv"):
for line in open("C:\km\hadoop\data\data_2d.csv"):
    row = line.split(',')
    sample = list(map(float, row))
    X.append(sample)

X = np.array(X)

X.shape

for line in X:
    print(line)

for i in range(len(X)):
    print("{} = {}".format(i, X[i]))
