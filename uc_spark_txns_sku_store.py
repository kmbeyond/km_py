'''
Program to generate the graph of sales of a product by store/city.
Input:
    -sku_id
Output:
    -Create a denormalized table of txn_dt, sku, store, qty

Author: Kiran Miryala/7897655

Steps:
1.Read from Hive/data files:
-data_rtl_txns.csv (txn_no,txn_dt,mem_num,store_id,sku_id,qty,paid)
-data_rtl_sku.csv (sku_id,sku_name,price)
-data_rtl_stores.csv (store_id,addr1,city,state)

2.Create a denormalized table of txn_dt, sku, store
3.Reports:
-Total Qty by Date, Store, Sku
-Total Qty by Date, Store, Sku for specific Sku
-Total Qty by Store, Sku

spark submit in local (AND use py3.5 because 3.6 gives error with Spark<=2.1.0):
source activate py35
spark-submit --master local ~/km/km_py/uc_spark_txns_sku_store.py

#on commandline
pyspark --master local

import uc_spark_txns_sku_store
uc_spark_txns_sku_store.main()

#using subprocess
exec(open("uc_spark_txns_sku_store.py").read()) #py3
execfile('uc_spark_txns_sku_store.py') #py2
#They appear in:
http://localhost:4040/jobs

'''

from pyspark.sql.functions import to_date
from pyspark.sql.types import IntegerType
from pyspark.sql import SparkSession

#def main():
    #using Spark session (in spark-submit only)
spark = SparkSession.builder \
    .master("local") \
    .appName("Txns SKU Store") \
    .getOrCreate()

    # .config("spark.some.config.option", "some-value") \

txnsDF = spark.read.format("csv").option("header","true"). \
    load('/home/kiran/km/km_hadoop/data/data_rtl_txns.csv')

storesDF = spark.read.format("csv").option("header","true"). \
    load('/home/kiran/km/km_hadoop/data/data_rtl_stores.csv'). \
    withColumnRenamed('addr1', 'store_addr1').withColumnRenamed('city', 'store_city').withColumnRenamed('state', 'store_state')

skuDF = spark.read.format("csv").option("header","true"). \
    load('/home/kiran/km/km_hadoop/data/data_rtl_sku.csv')

'''

#OR: using SQLContext
txnsDF = sqlContext.read.load('/home/kiran/km/km_hadoop/data/data_rtl_txns.csv',
                      format='com.databricks.spark.csv',
                      header='true',
                      inferSchema='true')


#OR: read from file (But this reads the header as record)
txnsDF2 = sc.textFile('/home/kiran/km/km_hadoop/data/data_rtl_txns.csv') \
.map(lambda s: s.split(",")) \
.map(lambda rec: (rec[0], rec[1], rec[2], rec[3], rec[5], rec[5], rec[6])) \
.toDF(["txn_no","txn_dt","mem_num","store_id","sku_id", "qty", "paid"])

'''
'''
#using HiveContext
from pyspark import SparkContext
import re, sys
sc = SparkContext("local", "Sales by Datetime/sku/store/qty")

from pyspark.sql import HiveContext
hc = HiveContext(sc)

txnsDF = hc.sql("select * from kmrtl.txns_stg")

storesDF = hc.sql("select * from kmrtl.stores").withColumnRenamed('addr1', 'store_addr1').withColumnRenamed('city', 'store_city').withColumnRenamed('state', 'store_state')

skuDF = hc.sql("select * from kmrtl.sku")

'''

#Extract date from datetime string
from pyspark.sql.functions import to_date
txnsDF2 = txnsDF.withColumn('txn_date2', to_date(txnsDF.txn_dt)).drop('txn_dt')
''' NOT WORKING
from_pattern = 'yyyy-MM-dd,  hh:mm:ss'
to_pattern = 'yyyy-MM-dd'
txnsDF.withColumn('txn_dt2', from_unixtime(unix_timestamp(txnsDF['txn_dt'], from_pattern), to_pattern)).show()
'''


#join txns & store
txnsStoreDF = txnsDF2.join(storesDF, "store_id")
#OR: txnsStoreDF = txnsDF.join(storesDF, [txnsDF.store_id==storesDF.store_id], "outer")
#Check data
#txnsStoreDF.count()
#txnsDF.join(storesDF, "store_id", "outer").filter(txnsStoreDF["addr1"] == "").count()
if(txnsDF.count() != txnsStoreDF.count()):
    print("Few records didn't join with store.")
#join with sku
txnsStoresSkuDF = txnsStoreDF.join(skuDF, "sku_id")
#check data
#txnsStoresSkuDF.count()
#txnsStoreDF.join(skuDF, "sku_id", "outer").filter(txnsStoresSkuDF["sku_name"] == "").count()
if(txnsDF.count() != txnsStoresSkuDF.count()):
    print("Few records didn't join with SKU.")


from pyspark.sql.types import IntegerType
txnsStoresSkuDF = txnsStoresSkuDF.withColumn("qty", txnsStoresSkuDF["qty"].cast(IntegerType()))

txnsStoresSkuDF.cache()

#group by txn_date, store_id, sku_id
soldSkuDF = txnsStoresSkuDF.groupBy("txn_date2", "store_id", "sku_id").sum("qty").withColumnRenamed('sum(qty)', 'qty_total')
soldSkuDF.show()

#filter by specific sku_id & group
txnsStoresSkuDF.filter(txnsStoresSkuDF["sku_id"]=="3456"). \
    groupBy("txn_date2", "store_id", "sku_id").sum("qty").withColumnRenamed('sum(qty)', 'qty_total').show()


#group by state, sku_id
soldStoreStateSkuDF = txnsStoresSkuDF.groupBy("store_state", "sku_id").sum("qty").withColumnRenamed('sum(qty)', 'qty_total')
soldStoreStateSkuDF.show()


#group by store_state
soldStoreStateSkuDF.show()

import matplotlib
#%matplotlib inline
txnsStoresSkuDFGph.plot()
matplotlib.pyplot.show(block=True)



#if __name__ == "__main__":
#    main()
