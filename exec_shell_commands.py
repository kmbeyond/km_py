


import subprocess
line_count = subprocess.check_output("cat dummy.txt | wc -l", shell=True).replace('\n','')
line_count
'3'


import os
os.system('cat dummy.txt | wc -l')
3 => row count
0 => the execution code (greater than 0 if errored)



from subprocess import PIPE, Popen
process = Popen( args='cat dummy.txt | wc -l', stdout=PIPE, shell=True ).communicate()
process[0].replace('\n','')
'3'
