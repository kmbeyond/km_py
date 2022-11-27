from datetime import datetime

#---easier way to get seconds & microseconds
time_start = datetime.now()

time_end = datetime.now()

time_diff = time_end-time_start

time_diff
datetime.timedelta(seconds=5832, microseconds=491302)
time_diff.seconds
#=> 5832
time_diff.total_seconds()
#=> 5832.491302


#---KM ops
def get_time_from_seconds(sec_total):
    ba=bytearray()
    ba.extend((str(int(sec_total/3600)).rjust(2,'0')+":").encode())
    ba.extend((str(int((sec_total/60)%60)).rjust(2,'0')+":").encode())
    ba.extend((str(int(sec_total%60)).rjust(2,'0')).encode())
    total_time=ba.decode()
    return total_time


#NOT COMPLETE YET
def get_time_from_ms(ms_total):
    ba=bytearray()
    ba.extend((str(int(ms_total/(3600000))).rjust(2,'0')+":").encode())
    ba.extend((str(int(((ms_total/60000)%60000)%60)).rjust(2,'0')+":").encode())
    #TO FIX THIS
    ba.extend((str(int((ms_total/36000)%60)).rjust(2,'0')).encode())
    total_time=ba.decode()
    return total_time


#using now()
time_start = datetime.now()
total=0
for i in range(10000000): total=total+i

print(total)
time_end = datetime.now()

time_diff = time_end-time_start
sec_diff = time_diff.seconds

str_dt_start = time_start.strftime('%Y-%m-%d %H:%M:%S')
str_dt_end = time_end.strftime('%Y-%m-%d %H:%M:%S')
print("Total time (",str_dt_start, " - ", str_dt_end, " = ", get_time_from_seconds(sec_diff))

ms_diff = time_diff.total_seconds() * 1000
print("Total time (",str_dt_start, " - ", str_dt_end, " = ", get_time_from_ms(ms_diff))



#using timestamp(in milliseconds)
ms_start = datetime.now().timestamp()
total=0
for i in range(10000000): total=total+i

print(total)
ms_end = datetime.now().timestamp()

sec_diff = int(ms_end-ms_start)

str_dt_start = datetime.fromtimestamp(ms_start).strftime('%Y-%m-%d %H:%M:%S')
str_dt_end = datetime.fromtimestamp(ms_end).strftime('%Y-%m-%d %H:%M:%S')
print("Total time (",str_dt_start, " - ", str_dt_end, " = ", get_time_from_seconds(sec_diff))

ms_diff = int(ms_end*1000 - ms_start*1000)
print("Total time (",str_dt_start, " - ", str_dt_end, " = ", get_time_from_ms(ms_diff))

