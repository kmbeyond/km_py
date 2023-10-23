
'''
DST rules: https://www.nist.gov/pml/time-and-frequency-division/popular-links/daylight-saving-time-dst

-begins at 2:00 a.m. on the second Sunday of March (at 2 a.m. the local time time skips ahead to 3 a.m. so there is one less hour in that day)
-ends at 2:00 a.m. on the first Sunday of November (at 2 a.m. the local time becomes 1 a.m. and that hour is repeated, so there is an extra hour in that day)
'''


from datetime import datetime
dt_string='2023-03-13'
dt_obj = datetime.strptime(dt_string, '%Y-%m-%d')
if dt_string.strip()=='': dt_obj = datetime.now()

#dt_today = date.today()
#dt_obj = dt_today
#dt_yesterday = dt_today - timedelta(days=1)
#dt_obj = dt_yesterday

from pytz import timezone
dst_dates = sorted([dt.strftime('%Y-%m-%d') for dt in timezone('America/Chicago')._utc_transition_times if dt.year==dt_obj.year])
dst_start,dst_end = dst_dates[0],dst_dates[1]

if dt_string in dst_dates:
    print('---DST switch DAY----')

if dt_string<dst_start: print('DST NOT Begun yet..')
elif dt_string==dst_start: print('-----DST Start date---')
elif dt_string>dst_start and dt_string<dst_end: print('DST')
elif dt_string==dst_end: print('-----DST Ending date----')
else: print('DST Ended')

