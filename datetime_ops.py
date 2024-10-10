
#--------------date-------------
from datetime import date
#date only
date.today().strftime('%Y-%m-%d')
#=> 2017-12-20


#--------------date time ----------------
from datetime import datetime
dt_now = datetime.now()
print(dt_now)
#=>2017-12-20 08:36:21.525668


print( dt_now.strftime( '%Y-%m-%d %H:%M:%S' ) )
#=> 2017-12-20 08:44:17

#Format timezone using '%Y-%m-%d %H:%M:%S %Z%z'
#=> 2002-10-27 12:00:00 CET+0100

#datetime in ISO format
dtISOformat = dt_now.isoformat()
#=> 2017-12-20T08:59:37.145674

#Specific part of datetime
dt_now.month
dt_now.year

#Scenario: Print Last Month & Year (Format: 2021-AUG)
dt_now = datetime.now()
last_month = dt_now.month - 1 if dt_now.month > 1 else 12
last_month_name = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][last_month-1]
year = dt_now.year-1 if last_month == 12 else now.year
print("Report for:", str(year)+"-"+last_month_name)


#Convert from date String to datetime object
dt1 = datetime.strptime("2007-12-25 23:44:56", "%Y-%m-%d %H:%M:%S")
print("String to Date obj: {}".format( dt1) )


#Ex: 12Hr format into 24Hr format
currDT='07:28:12 PM'
dtObj = datetime.strptime(currDT, '%I:%M:%S %p')
print("24 hr format ({}) =".format(currDT), dtObj.strftime('%H:%M:%S') )

#---add/subtract days/hours to a date
from datetime import date, datetime, timedelta
yesterday_date = (date.today()-timedelta(days=1)).strftime('%Y-%m-%d')
yesterday_date = (datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d')

last_run_date = '2021-11-29'
previous_date = (datetime.strptime(last_run_date, "%Y-%m-%d")-timedelta(days=1)).strftime('%Y-%m-%d')

#----difference between 2 dates

#using now()
time_start = datetime.now()

time_end = datetime.now()

time_diff = time_end-time_start
#=>datetime.timedelta(seconds=5832, microseconds=491302)

time_diff.seconds
#=> 5832
time_diff.total_seconds()
#=> 5832.491302



#-----------------------milli/micro seconds
#------timestamp (time in milliseconds)
from datetime import datetime
ts = datetime.now().timestamp()
print(f"current timestamp: {ts}")
#=>current timestamp: 1663859078.253567

#IMP: to get unix/epoch time that is used mostly for logging
int(datetime.now().timestamp())
#OR using time
import time
int(time.mktime(datetime.now().timetuple()))


#get formatted datetime from a timestamp data
datetime.fromtimestamp(1663859078).strftime('%Y-%m-%d %H:%M:%S')
#=>2022-09-22 10:04:38

#USE CASE: time difference between 2 datetimes
ts_start = datetime.now().timestamp()
ts_end = datetime.now().timestamp()
#time diff
sec_diff = int(ts_end - ts_start)
ms_total = int(ts_end*1000 - ts_start*1000)



#-----time
import time
time_current = time.time()
#=>current time: 1663858767.2510579

#to rounded milliseconds (10 digits)
ms_current = round(time_current)
print("time in milliseconds=", ms_current )
#=> time in milliseconds= 1663856362

time_in_ms = 1646380381322
#NOTE: if timestamp more than 10 digits, divide by appropriate 10s
dt = datetime.fromtimestamp(time_in_ms/1000)


#timestamp/ms into time
print(datetime.fromtimestamp(time_current))
=> 2022-09-22 10:08:09.391967

#to format date
print(datetime.fromtimestamp(time_current).strftime('%Y-%m-%d %H:%M:%S') )
=> 2022-09-22 10:13:29


#---get past/future timestamp
past_hours=1
ms_back = round( (time.time()-(60 * 60 * past_hours)) )
print(datetime.fromtimestamp(ms_back))
print(f"Time in last {past_hours} hour(s): {ms_back} -> {ms_current}")
=> Time in last 1 hour(s): 1663856013 -> 1663859613

print(f"Time in last {past_hours} hour(s): {datetime.fromtimestamp(ms_back)} -> {datetime.fromtimestamp(ts)}")
=> Time in last 1 hour(s): 2022-09-22 10:13:33 -> 2022-09-22 11:13:32.858255

#using timedelta
print(datetime.now())
=>2022-09-22 11:20:51.181308
print(datetime.now() + timedelta(hours=5))
=>2022-09-22 16:20:51.181308


#-------------Timezones & UTC/GMT-----
from datetime import datetime
datetime.now() #--> local timezone

#pytz: needs installing pytz library (using pip)
import pytz #import timezone

#--to EST
datetime.now(pytz.timezone("America/New_York"))
datetime.now().astimezone(pytz.timezone('America/New_York'))

#--to UTC
datetime.now(pytz.timezone("UTC"))
datetime.now().astimezone(pytz.timezone('UTC'))
datetime.now(pytz.utc)

dtUTC = datetime.now(pytz.utc)
dtUTC.strftime('%Y-%m-%d %H:%M:%S %Z')
#=> 2017-12-20 14:50:37 UTC
dtUTC.strftime('%Y-%m-%d %H:%M:%S %z')
#=> 2017-12-20 14:50:37 +0000


cst = pytz.timezone('US/Central')
chicagotz = pytz.timezone('America/Chicago')
latz = pytz.timezone('America/Los_Angeles')
datetime.now(latz).strftime('%Y-%m-%d %H:%M:%S %z')
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

#-----from military to 12hr format
def to_12_hour_format(str_military):
 #str_military='13:12:33'
 hr,mi,sc = str_military[0:2], str_military[3:5], str_military[6:8]
 am = 'AM' if int(hr) <= 12 else 'PM'
 hr = int(hr)-12 if int(hr)>=12 else int(hr)
 hr = 12 if hr==0 else hr
 hr = str(hr).zfill(2)
 return (':'.join([str(hr),mi,sc]))+am

print(to_12_hour_format('13:12:33'))
print(to_12_hour_format('12:12:33'))
print(to_12_hour_format('07:12:33'))

#using datetime functions
dt = datetime.strptime('13:12:33', '%H:%M:%S')
print(dt.strftime('%I:%M:%S %p'))
