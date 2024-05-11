import pandas as pd
pd.set_option('display.max_columns', None)

#--transactions
txnsdf = pd.read_csv("/home/km/km/km_practice/data/data_rtl_txns.csv").set_index('store_id')
txnsdf.head()

#--stores/merchants
storesdf = pd.read_csv("/home/km/km/km_practice/data/data_rtl_stores.csv")
storesdf.head()

store_trans_df = txnsdf.groupby(['store_id']).agg(total_rows=('paid', 'size'),
                                                  total_amount=('paid', 'sum'))
store_trans_df = txnsdf.groupby(['store_id']).paid.agg('sum').to_frame('total_amount')
#store_trans_df = txnsdf.groupby(['store_id']).agg({'paid': ['size', 'sum']})
store_trans_df.head()

#calc amount percentage of each mcc
store_trans_df['amount_perc'] = round((store_trans_df['total_amount']/store_trans_df['total_amount'].sum())*100, 2)
store_trans_df.head()

#--specific MCC codes
store_trans_df_s327 = store_trans_df[store_trans_df['store_id'] == 'S327']
store_trans_df_s327.head()
store_trans_df_s327_s3695 = store_trans_df[store_trans_df['store_id'].isin(['S327', 'S3695'])]
store_trans_df_s327_s3695.head()


#-----Join both dataframes - multiple ways
store_trans_joined = storesdf.merge(txnsdf, on=['store_id'], how='left').set_index('store_id')
store_trans_joined.groupby(['store_id']).agg(total_rows=('paid', 'size'), total_amount=('paid', 'sum')).head()

store_trans_joined2 = pd.merge(storesdf, txnsdf, left_on=['store_id'], right_on=['store_id']).set_index('store_id')
store_trans_joined2.head(10)
store_trans_joined2.groupby(['store_id']).agg(total_rows=('paid', 'size'), total_amount=('paid', 'sum')).head()

#Join by indexing
store_trans_joined3 = storesdf.set_index('store_id').join(txnsdf)
store_trans_joined3.head(5)
store_trans_joined3.groupby(['store_id']).agg({'paid': ['size', 'sum']}).head()


