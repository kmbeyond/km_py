'''
Program to merge the parts with new categories.
Input:

Output:
    -Writes the merged csv file to output directory

Author: Kiran Miryala/7897655

Steps:
1.Read from data files into dataframes:
-data_part_categories_mast.txt
    part_num,name,categories
    P1001,Part 1001,[Cat001,Cat003,Cat006]
    P1002,Part 1002,[Cat005,Cat004,Cat008]

-data_part_categories_add.txt (sku_id,sku_name,price)
    P1002,[Cat100]
    P1004,[Cat10,Cat12]


2.Convert the String to Array type & merge both into an array
3.Write the merged dataframe

spark submit in local (AND use py3.5 because 3.6 gives error with Spark<=2.1.0):
cd km/km_py
source activate py35
spark-submit --master local ~/km/km_py/uc_spark_parts_cats_merge_save.py
source deactivate

#on commandline
pyspark --master local

import uc_spark_parts_cats_merge_save
uc_spark_parts_cats_merge_save.main()

#using subprocess
exec(open("uc_spark_parts_cats_merge_save.py").read()) #py3
execfile('uc_spark_parts_cats_merge_save.py') #py2
#They appear in:
http://localhost:4040/jobs

'''

from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat_ws, split, regexp_extract,udf


#def main():
    #using Spark session (in spark-submit only)
spark = SparkSession.builder \
    .master("local") \
    .appName("Txns SKU Store") \
    .getOrCreate()

    # .config("spark.some.config.option", "some-value") \
sc = spark.sparkContext
sqlContext = SQLContext(sc)

sInputDirPath="/home/kiran/km/km_big_data/data/"
sOutputDirPath="/home/kiran/km/km_hadoop_op/op_spark/"

#Read as string & extract using regex
dfPartCatsMasterFile = sqlContext.read.text(sInputDirPath+"data_part_categories_mast.txt")
dfPartCatsMasterFile.show(5)


#Used http://www.pyregex.com/
dfPartCatsMaster = dfPartCatsMasterFile.select(regexp_extract('value', r'^([\w_]+),', 1).alias("part_num"), \
        regexp_extract('value', r'^[\w_]+,([\w ]+),', 1).alias("name"), \
        regexp_extract('value', r'^[\w_]+,[\w ]+,\[([\w, ]+)\]', 1).alias("categories")  ). \
    filter(col('part_num') != "part_num"). \
    withColumn("cat_list", split(col("categories"), ",\s*").cast("array<string>").alias("cat_list") ). \
    drop("categories")


dfPartCatsAddFile = sqlContext.read.text(sInputDirPath+"data_part_categories_add.txt")
dfPartCatsAddFile.show(5)


#Used http://www.pyregex.com/
dfPartCatsAdd = dfPartCatsAddFile.select(regexp_extract('value', r'^([\w_]+),', 1).alias("part_num"), \
        regexp_extract('value', r'^[\w_]+,\[([\w, ]+)\]', 1).alias("categories")  ). \
    filter(col('part_num') != "part_num"). \
    withColumn("cat_list_new", split(col("categories"), ",\s*").cast("array<string>") ). \
    drop("categories")

dfPartCatsAdd.show(10)

dfPartCatsMasterAdd = dfPartCatsMaster.join(dfPartCatsAdd, "part_num")

#Merge both lists
from itertools import chain
from pyspark.sql.types import ArrayType, StringType

def concat(type):
    def concat_(*args):
        return list(chain(*args))
    return udf(concat_, ArrayType(type))

concat_string_arrays = concat(StringType())

dfPartCatsMasterAddMerged = dfPartCatsMasterAdd.select(col("part_num"), concat_string_arrays(col("cat_list"), col("cat_list_new")).alias("cat_list_merged"))
#dfPartCatsMasterAddMerged = dfPartCatsMasterAdd.withColumn("cat_list_merged", concat_string_arrays(col("cat_list"), col("cat_list_new")))

dfPartCatsMasterAddMerged2 = dfPartCatsMasterAddMerged.withColumn("cat_list_merged_str", concat_ws(',', col('cat_list_merged'))).alias("single_col"). \
    drop("cat_list_merged")

dfPartCatsMasterAddMerged2.write.csv(sOutputDirPath+"data_part_categories_mast_new")
#P1002,"Cat005,Cat004,Cat008,Cat100"
#P1004,"Cat013,Cat001,Cat005,Cat10,Cat12"

