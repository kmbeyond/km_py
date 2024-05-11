import pandas as pd
pd.set_option('display.max_columns', None)

#--transactions
txnsdf = pd.read_csv("/home/km/km/km_practice/data/data_rtl_txns.csv").set_index('store_id')
txnsdf.head()

#--stores/merchants
storesdf = pd.read_csv("/home/km/km/km_practice/data/data_rtl_stores.csv")
storesdf.head(10)

store_trans_df = txnsdf.groupby(['store_id']).agg(total_amount=('paid', 'sum'))
#store_trans_df = txnsdf.groupby(['store_id']).paid.agg('sum').to_frame('total_amount').head(10)
store_trans_df.head(20)

#-----Join trans total & Merch
store_trans_joined = storesdf.merge(store_trans_df, on=['store_id'], how='left').set_index('store_id')
store_trans_joined.head(20)


storesdf.set_index('mcc')
mcc_totals_df = store_trans_joined.set_index('mcc').groupby(['mcc']).agg(total_mcc_amount=('total_amount', 'sum'))
mcc_totals_df.head(10)
mcc_totals_df.dtypes
mcc_totals_df.columns

#mcc_metrics_df['mcc'] = mcc_metrics_df['mcc'].astype(str)
mcc_totals_df.index = mcc_totals_df.index.map(str)

#card types
cards_df = pd.read_csv("/home/km/km/km_practice/data/data_rtl_card_mcc_cashbacks.csv")
cards_df.head()

cards_df_mcc = cards_df[cards_df['mcc'] != 'OTHER']
cards_df_other = cards_df[cards_df['mcc'] == 'OTHER']

cards_cb_df = mcc_totals_df.merge(cards_df_mcc, on=['mcc'], how='left')
cards_cb_df.head(10)
len(cards_cb_df.index)

#set OTHER if no matched MCC
cards_cb_df.loc[cards_cb_df.card_type.isnull(), 'mcc'] = "OTHER"

cards_cb_df_mcc = cards_cb_df[cards_cb_df['mcc'] != 'OTHER']
cards_cb_df_other = cards_cb_df[cards_cb_df['mcc'] == 'OTHER']
cards_cb_df_other = cards_cb_df_other.drop(['card_type', 'cashback_percent'], axis=1)

cards_cb_df_other2 = cards_cb_df_other.merge(cards_df_other, on=['mcc'], how='left')
cards_cb_df_other2.head()

#union/merge/append both dataframes
cards_cb_df_final = pd.concat([cards_cb_df_mcc, cards_cb_df_other2])
#cards_cb_df_final = pd.merge(cards_cb_df_mcc, cards_cb_df_other2, how='outer')
cards_cb_df_final.head(10)

#calc cashback amount
cards_cb_df_final['cashback'] = round(cards_cb_df_final.total_mcc_amount * cards_cb_df_final.cashback_percent/100, 2)
cards_cb_df_final.head(10)

cards_cb_df_final.set_index('card_type', inplace=True)
cards_cb_df_final.sort_index(inplace=True)
cards_cb_df_final.head(20)

cards_cb_df_final.groupby(['card_type']).agg(total_cashback=('cashback', 'sum'))

