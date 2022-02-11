


#-----loop by string comparison
from datetime import datetime, date, timedelta
sDateFrom = '2022-01-01'
sDateTo = '2022-01-29'
increments = 6

loop_from = sDateFrom
loop_to = (datetime.strptime(loop_from, '%Y-%m-%d') + timedelta(days=increments)).strftime( '%Y-%m-%d' )
while loop_from <= sDateTo:
 loop_from = sDateTo if loop_from > sDateTo else loop_from
 loop_to = sDateTo if loop_to > sDateTo else loop_to
 print("Dates: {} - {}".format(loop_from, loop_to))
 #process
 loop_from = (datetime.strptime(loop_to, '%Y-%m-%d') + timedelta(days=1)).strftime( '%Y-%m-%d' )
 loop_to = (datetime.strptime(loop_from, '%Y-%m-%d') + timedelta(days=increments)).strftime( '%Y-%m-%d' )















 
