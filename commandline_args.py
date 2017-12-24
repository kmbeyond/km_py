


print("Main: {}".format(__name__))


import sys

for l in range(len(sys.argv)):
    print("args {}: {}".format(l, sys.argv[l]))

#Output:
#$ python commandline_args.py aa bb cc
#args 0: commandline_args.py
#args 1: aa
#args 2: bb
#args 3: cc



def print_all_args(*args):
    print(args)
