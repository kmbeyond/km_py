

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
 
 
