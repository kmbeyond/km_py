
#Time formatting
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
#=> 2002-10-27 12:00:00 CET+0100


##using now() to get current datetime
import datetime
now = datetime.datetime.now()
print("Current datetime: {}".format( now ) )

from datetime import datetime
now = datetime.now()
print("Current datetime: {}".format( now ) )
#=> Current datetime: 2017-12-20 08:42:26.178157

dtFormatted = datetime.now().strftime( fmt )
print("Current datetime formatted: {}".format( dtFormatted ) )
#=> Current datetime formatted: 2017-12-20 08:44:17

#Convert from date object(s) to String
sNow = str(now)
print("Date obj to String: {}".format( sNow ) )
#=>2017-12-20 08:36:21.525668

#Convert from date String to object(s)
dt1 = datetime.strptime("2007-12-25 23:44:56", "%Y-%m-%d %H:%M:%S")
print("String to Date obj: {}".format( dt1) )

#datetime in ISO format
dtISOformat = datetime.now().isoformat()
#=> 2017-12-20T08:59:37.145674

#current time in milliseconds
int(round(time.time() * 1000))



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
datetime.now(chicagotz).strftime(fmt)
#=> 2017-12-20 09:33:56 CST-0600

latz = pytz.timezone('America/Los_Angeles')
datetime.now(latz).strftime(fmt)
#=> m2017-12-20 07:35:01 PST-0800

#Time diff
timediff = ((datetime.now(timezone.utc)-datetime.now(cst)))

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
