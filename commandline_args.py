
'''
Test commandline arguments

Ex: Execute:
$python commandline_args.py aa bb cc
#args 0: commandline_args.py
#args 1: aa
#args 2: bb
#args 3: cc

'''

print("Method: {}".format(__name__))


import sys

for l in range(len(sys.argv)):
    print("argv[{}] : {}".format(l, sys.argv[l]))


#Define method to print list
def print_all_args(args):
    for l in range(len(args)):
        print("args[{}] : {}".format(l, args[l]))


print("Args using method:")
print_all_args(sys.argv)