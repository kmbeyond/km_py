


print("------------ Simple Class attributes -------")
class Person:
    num_eyes = 2

print("Person.num_eyes=",Person.num_eyes)
#=> 2

p1 = Person()
print("p1.num_eyes=", p1.num_eyes)
#= > 2

Person.num_eyes = 1
p2 = Person()
print("p2.num_eyes=", p2.num_eyes)
#=> 1

#Change value using the instance
p2.num_eyes = 3
print("p2.num_eyes=",p2.num_eyes) #=> 3; because this creates an instance variable; static is not changed
print("p1.num_eyes=", p1.num_eyes) #=> 1; because any change by p2 doesn't change the static
#= > 1
print("Person.num_eyes=", Person.num_eyes) #=> 1





print("------------ Instance attributes -------------")
class Person2:
	def __init__(self, eyes):
           self.num_eyes=eyes

p1=Person2(2)
print(p1.num_eyes) #=>2
p2=Person2(1)
print(p2.num_eyes) #=>1




print("------------ Both Class & instance variables usage -------------")

class Foo:
    staticList = None # Static: visible to all classes
    def __init__(self, name, x):
        self.name = name #instance variable
        if not Foo.staticList:
            Foo.staticList = [] # New local version for this object
        #Foo.staticList.append(x)
        self.staticList.append(x) #Using same static variable

    def f(self, x):
        #Foo.staticList.append(x)
        self.staticList.append(x) #Using same static variable

    def __str__(self):
        return "name= {}; self staticList= {}; class staticList= {}".format(self.name, self.staticList, Foo.staticList)

f1 = Foo("first", 10)
print(f1)
f1.f(15)
print(f1)

f2 = Foo("second", 20)
print(f2)
f2.f(25)
print(f2)

print(Foo.staticList)

Foo.staticList.append(30)

print(Foo.staticList)

print("Initializing the staticList using f1:")
f1.staticList = [11,22]
print(f1)
print(Foo.staticList)
