
from datetime import datetime, date, timedelta
def getDT():
 return datetime.now().strftime( '%Y-%m-%d %H:%M:%S')

days_total=int(50)
increments=int(7)

lowLimit=6
upperLimit=lowLimit+increments

while lowLimit <= days_total:
 upperLimit = days_total if upperLimit>days_total else upperLimit
 print("{}: range: {} - {}".format(getDT(), lowLimit, upperLimit) )
 #Other operations
 
 lowLimit=upperLimit+1
 upperLimit=lowLimit+increments
 
 
upperLimit=days_total
lowLimit=upperLimit-increments

while upperLimit >= 1:
 lowLimit=1 if lowLimit<1 else lowLimit
 print("{}: Days range: {} - {}".format(getDT(), lowLimit, upperLimit) )
 
 upperLimit=lowLimit-1
 lowLimit=upperLimit-increments
