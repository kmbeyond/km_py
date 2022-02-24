
from datetime import datetime, date, timedelta
def getDT():
 return datetime.now().strftime( '%Y-%m-%d %H:%M:%S')


days_total = 50
increments = 5

# ----Ascend: Low to High
print("------ Low to High ------")
lowLimit = 6
upperLimit = lowLimit + increments -1

while lowLimit <= days_total:
    upperLimit = days_total if upperLimit > days_total else upperLimit
    print(f"{getDT()}: Range: {lowLimit} - {upperLimit}")
    # Other operations

    lowLimit = upperLimit + 1
    upperLimit = upperLimit + increments

'''#Similar
#start_count = 1
end_count = 100

loop_start = 21
increments = 5
loop_end = loop_start+increments -1
#loop_end = 25

while (loop_start <= end_count):
    loop_start = end_count if loop_start > end_count else loop_start
    loop_end = end_count if loop_end > end_count else loop_end
    print(getDT() + ": Loop for: " + str(loop_start) + " -> " + str(loop_end))


    loop_start = loop_end + 1
    loop_end = loop_end + increments

'''

# ----Descend: High to Low
print("------ High to Low ------")
days_total = 50
decrements = 5

upperLimit = days_total
lowLimit = upperLimit - decrements + 1

while upperLimit >= 1:
    lowLimit = 1 if lowLimit < 1 else lowLimit
    print(f"{getDT()}: Range: {upperLimit} - {lowLimit}")

    upperLimit = lowLimit - 1
    lowLimit = lowLimit - decrements



# ----iterate/loop between dates (old date to current)
print("------ DATES: Current to backwards ------")
increments = int(30)
s_dt_oldest = '2020-01-01'

lowLimit = 1
upperLimit = lowLimit + increments
s_dt_from = (date.today() - timedelta(upperLimit)).strftime('%Y-%m-%d')

while s_dt_from > s_dt_oldest:
    s_dt_from = (date.today() - timedelta(upperLimit)).strftime('%Y-%m-%d')
    s_dt_to = (date.today() - timedelta(lowLimit)).strftime('%Y-%m-%d')
    s_dt_from = s_dt_oldest if s_dt_oldest > s_dt_from else s_dt_from
    print(f"{getDT()}:  ---> Days Range: {s_dt_to}({upperLimit}) - {s_dt_from}({lowLimit})")
    lowLimit = upperLimit + 1
    upperLimit = upperLimit + increments


 
