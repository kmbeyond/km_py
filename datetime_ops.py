
#--------------date-------------
from datetime import date
#date only
date.today().strftime('%Y-%m-%d')
#=> 2017-12-20


#--------------date time ----------------
from datetime import datetime
now = datetime.now()

#Convert from date object(s) to String
#sNow = str(now)
print("{}".format( now ) )
#=>2017-12-20 08:36:21.525668

dtFormatted = datetime.now().strftime( '%Y-%m-%d %H:%M:%S' )
print("Current datetime: {}".format( dtFormatted ) )
#=> Current datetime: 2017-12-20 08:44:17

#Format timezone using '%Y-%m-%d %H:%M:%S %Z%z'
#=> 2002-10-27 12:00:00 CET+0100

#datetime in ISO format
dtISOformat = datetime.now().isoformat()
#=> 2017-12-20T08:59:37.145674

#Specific part of datetime
now.month
now.year

#Scenario: Print Last Month & Year (Format: 2021-AUG
last_month = now.month - 1 if now.month > 1 else 12
last_month_name = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][last_month-1]
year = now.year-1 if last_month == 12 else now.year
print("Report for:" +str(year)+"-"+last_month_name)

#------------Conversion--------------

#Convert 12Hr format into 24Hr format
currDT='07:28:12 PM'
dtObj = datetime.strptime(currDT, '%I:%M:%S %p')
print("24 hr format ({}) =".format(currDT), dtObj.strftime('%H:%M:%S') )


#Convert from date String to object(s)
dt1 = datetime.strptime("2007-12-25 23:44:56", "%Y-%m-%d %H:%M:%S")
print("String to Date obj: {}".format( dt1) )



#current time in milliseconds
import time
print("time in milliseconds=", int(round(time.time() * 1000)) )



#-------------Timezones & UTC/GMT-----
import pytz
dtUTC = datetime.now(pytz.utc)
dtUTC.strftime('%Y-%m-%d %H:%M:%S')
#=> 2017-12-20 14:47:38

from datetime import timezone
dtUTC2 = datetime.now(timezone.utc)
dtUTC.strftime('%Y-%m-%d %H:%M:%S %Z')
#=> 2017-12-20 14:50:37 UTC

dtUTC.strftime('%Y-%m-%d %H:%M:%S %z')
#=> 2017-12-20 14:50:37 +0000

cst = pytz.timezone('US/Central')
datetime.now(cst).strftime(fmt)
#=> 2017-12-20 09:31:56 CST-0600

chicagotz = pytz.timezone('America/Chicago')
print("America/Chicago=", datetime.now(chicagotz).strftime(fmt))
#=> 2017-12-20 09:33:56 CST-0600

latz = pytz.timezone('America/Los_Angeles')
datetime.now(latz).strftime(fmt)
#=> m2017-12-20 07:35:01 PST-0800

#Time diff
timediff = ((datetime.now(timezone.utc)-datetime.now(cst)))
print("Time diff=", timediff)

import time
print("GMT: {}".format( time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) ))
#print("GMT: {}".format( datetime.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) ))


#print("Current datetime: {}".format(datetime.strftime("%Y-%m-%d %H:%M:%S", datetime.now()) ) )


#NOTES: time.strftime() converts datetime object to string format
#       time.strptime() converts datetime string to datetime object
#       datetime.strftime() converts datetime string to datetime object
#       datetime.strptime() converts datetime object to string format


import os
print("Timezone: {}".format( time.tzname ) )
