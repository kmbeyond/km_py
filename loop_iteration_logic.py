
from datetime import datetime, date, timedelta
def getDT():
 return datetime.now().strftime( '%Y-%m-%d %H:%M:%S')

days_total=int(50)
increments=int(7)

#----Ascend: Low to High
lowLimit=6
upperLimit=lowLimit+increments

while lowLimit <= days_total:
 upperLimit = days_total if upperLimit>days_total else upperLimit
 print("{}: range: {} - {}".format(getDT(), lowLimit, upperLimit) )
 #Other operations
 
 lowLimit=upperLimit+1
 upperLimit=lowLimit+increments
 

 #----Descend: High to Low
upperLimit=days_total
lowLimit=upperLimit-increments

while upperLimit >= 1:
 lowLimit=1 if lowLimit<1 else lowLimit
 print("{}: Days range: {} - {}".format(getDT(), lowLimit, upperLimit) )
 
 upperLimit=lowLimit-1
 lowLimit=upperLimit-increments

 
 #----iterate/loop between dates (old date to current)
increments=int(30)
sDateFrom='2020-02-05'

lowLimit=1
upperLimit=lowLimit+increments
s_dt_from = (date.today()-timedelta(upperLimit)).strftime('%Y-%m-%d')

while s_dt_from > sDateFrom:
 s_dt_from = (date.today()-timedelta(upperLimit)).strftime('%Y-%m-%d')
 s_dt_to = (date.today()-timedelta(lowLimit)).strftime('%Y-%m-%d')
 s_dt_from = sDateFrom if sDateFrom>s_dt_from else s_dt_from
 print("{}:  ---> Days Range: {}({}) - {}({})".format(getDT(), s_dt_from, lowLimit, s_dt_to, upperLimit) )
 lowLimit=upperLimit+1
 upperLimit=lowLimit+increments
 
