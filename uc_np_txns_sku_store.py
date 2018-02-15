
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

'''

import pandas as pd
txnsDF = pd.read_csv("/home/kiran/km/km_hadoop/data/data_rtl_txns.csv")

#stores
storesDF = pd.read_csv("/home/kiran/km/km_hadoop/data/data_rtl_stores.csv"). \
    rename(columns={'addr1': 'store_addr1'}). \
    rename(columns={'city': 'store_city'}). \
    rename(columns={'state': 'store_state'})
#sku
skuDF = pd.read_csv('/home/kiran/km/km_hadoop/data/data_rtl_sku.csv')




#Extract date from datetime string
from datetime import datetime
txnsDF['txn_date2'] = txnsDF['txn_dt'].apply(lambda x: datetime.strftime(datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d"))
#NOTES:
#       datetime.strftime() converts datetime string to datetime object
#       datetime.strptime() converts datetime object to string format
#       time.strftime() converts datetime object to string format
#       time.strptime() converts datetime string to datetime object

txnsDF2 = txnsDF.drop('txn_dt', axis=1)



#join txns & store
txnsStoreDF = txnsDF2.set_index('store_id').join(storesDF.set_index('store_id')).reset_index()
#txnsStoreDF['store_id']=txnsStoreDF.index #used instead of reset_index()

#OR: txnsStoreDF = txnsDF.join(storesDF, [txnsDF.store_id==storesDF.store_id], "outer")
#Check data
#len(txnsStoreDF.txn_no)
#txnsDF.join(storesDF, "store_id", "outer").filter(txnsStoreDF["addr1"] == "").count()
if(len(txnsDF.txn_no) != len(txnsStoreDF.txn_no)):
    print("Few records didn't join with store.")

#join with sku
txnsStoresSkuDF = txnsStoreDF.set_index('sku_id').join(skuDF.set_index('sku_id')).reset_index()
#txnsStoresSkuDF['sku_id']=txnsStoresSkuDF.index #used instead of reset_index()
#check data
#len(txnsStoresSkuDF.txn_no)
#txnsStoreDF.join(skuDF, "sku_id", "outer").filter(txnsStoresSkuDF["sku_name"] == "").count()
if(len(txnsDF.txn_no) != len(txnsStoresSkuDF.txn_no)):
    print("Few records didn't join with SKU.")


#group by txn_date, store_id, sku_id
grpByCols=["txn_date2", "store_id", "sku_id"]
soldSkuDF = txnsStoresSkuDF.groupby(grpByCols).agg({'qty' : 'sum'}).reset_index()

#filter by specific sku_id & group

txnsStoresSkuDF[txnsStoresSkuDF["sku_id"]==3456]. \
    groupby(["txn_date2", "store_id", "sku_id"]).agg({'qty' : 'sum'}).reset_index()


#group by state, sku_id
soldStoreStateSkuDF = txnsStoresSkuDF.groupby(["store_state", "sku_id"]).agg({'qty' : 'sum'}).reset_index()

soldStoreStateSkuDF.head()

from tabulate import tabulate
print(tabulate(soldStoreStateSkuDF, headers='keys', tablefmt='psql'))

#This prints only header
#for rec in soldStoreStateSkuDF:
#    print(rec)




#Get matplotlib
import matplotlib
#%matplotlib inline
#ipython = get_ipython()


#soldStoreStateSkuDF.plot()
#matplotlib.pyplot.show(block=True)
