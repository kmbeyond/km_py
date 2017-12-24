#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 8 08:34:55 2017

@author: kiran
"""

class Student:
    #constructor
    def __init__(self, name, school, marks):
        self.name=name
        self.school=school
        if(marks != None):
            self.marks = []
            for x in marks:
                self.marks.append(x)
        print("Called: constructor on :{}".format(self.name))

    #destructor
    def __del__(self):
        print("Called: destructor on :{}".format(self.name))
        self.marks=[]
        pass

    def remove(self):
        print("Called: remove")
        self._finalizer()

    def printMe(self):
        print("I am {}, from {} School & my marks {}".format(self.name,self.school,str(self.marks)))


print('Creating instance..')
anna = Student("Anna", "MIT", [60])
anna.printMe()


print("anna is instance of Student: {}".format(isinstance(anna, Student)))

print("Explicitly destroying object...")
anna=None
print("is anna dereferenced: {}".format((True if anna is None else False))) #True
del anna
#print("is anna dereferenced: {}".format((True if anna is None else False))) #This gives error
print("Explicit destroy completed.")


print('Circular referencing....')
class Foo:
	def __init__(self, x):
		print ("Foo: Hi")
		self.x = x
	def __del__(self):
		print ("Foo: bye")

class Bar:
	def __init__(self):
		print ("Bar: Hi")
		self.foo = Foo(self) # x = this instance

	def __del__(self):
		print ("Bar: Bye")

bar = Bar()
#del bar # This doesn't work either.

bar = None
print("is bar dereferenced: {}".format((True if bar is None else False)))
del bar
print("is bar dereferenced: {}".format((True if bar is None else False)))
