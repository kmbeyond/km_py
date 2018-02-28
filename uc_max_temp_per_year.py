import pandas as pd

fileDF = pd.read_csv("/home/kiran/km/km_hadoop/data/data_year_max_temp.csv",
                     header=0, sep=",", skip_blank_lines=True, low_memory=False)
            #names=["year", "max_temp", "quality"]


print("-----head5 records: fileDF\n{}".format(fileDF.head(5)))
print("-----count: \n{}".format(fileDF.count()))
#print(fileDF.keys())

print("-----dtypes:\n {}".format(fileDF.dtypes))


qualityRecDF = fileDF.loc[fileDF['quality'] != 9999]
#qualityRecDF = fileDF.query('quality != 9999')


print("-----head5 records: qualityRecDF\n{}".format(qualityRecDF.head(10)))
print("-----count: \n{}".format(qualityRecDF.count()))

print("-----describe:\n{}".format(fileDF.describe()))

#print("-----axes:\n{}".format(fileDF.axes))
