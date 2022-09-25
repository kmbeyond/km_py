#arguments
#Execution: python py_args.py 1 2
# Wrong inputs: python py_args.py 1 2
# echo $? => 5

import sys
for i in range(len(sys.argv)):
 print(f"{i} : {sys.argv[i]}")

if (len(sys.argv) != 3):
 print("ERROR: Wrong input: Must be 2 arguments")
 #raise ValueError("Must be 2 arguments")
 sys.exit(5)


print('Script starts')

