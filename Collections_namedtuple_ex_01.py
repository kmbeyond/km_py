
from collections import namedtuple




empRec = namedtuple('EmployeeRec', 'name, age, title, department, paygrade', verbose=True)


e1 = empRec("John", 25, "Engineer", "IT", "A2")
print("Employee: {}; Age={}; title:{}".format( e1.name, e1.age, e1.title) )


print("------ read from file & assign values directly -----")
sEmpFile = "/home/kiran/km/km_hadoop/data/data_employeerecord_nameddtuple.csv"
#Sample data:
#John, 25,Engineer, IT, A2
#Kevin, 27,Developer, IT, A3

import csv
for emp in map(empRec._make, csv.reader(open(sEmpFile, "r"))):
    print(emp.name, emp.title)




print("-------  Define a Point type namedtuple  ------")
pt = namedtuple('Point', 'x y')
pt1 = pt(1.0, 5.0)


p = pt(11, y=22)     # instantiate with positional or keyword arguments
print(p[0] + p[1])             # indexable like the plain tuple (11, 22)
#33

x, y = p                # unpack like a regular tuple
print("{}, {}".format(x, y) )

#=>(11, 22)


print(p.x + p.y)               # fields also accessible by name
#=>33

print(p)                       # readable __repr__ with a name=value style
#=> Point(x=11, y=22)
