#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:57:29 2017

@author: kiran
"""

class Student:
    def __init__(self, name, school, marks):
        self.name=name
        self.school=school
        if(marks != None):
            self.marks = []
            for x in marks:
                self.marks.append(x)

    def printMe(self):
        print("About Me: ")
        print("I am {}, from {} School & my marks {}".format(self.name,self.school,str(self.marks)))

    def average(self):
        return sum(self.marks)/len(self.marks)

    def tellYourSchool(self):
        print("method: I'm going to school - "+self.name)

    @classmethod
    def tellYourSchool_classMethod(cls): #This passes class instead of object
        print("classmethod:I'm going to school")
        print("            I'm {}".format(cls))

    @staticmethod
    def tellYourSchool_staticMethod(): #This passes no object
        print("staticmethod: I'm going to school")

    def friend(self, name):
        return Student(name, self.school, [])

    @classmethod
    def friend_classMethod(cls, origin, name):
        obj = cls(name, origin.school, [])
        obj.printMe()
        return obj



#inheritence
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school, [])
        self.salary=salary

    def printMe(self):
        print("About Me: ")
        print("I am {}, studied at {} School & my salary {}".format(self.name,self.school,self.salary))

print("Inheritence:")
greg=WorkingStudent("Greg", "MIT", 2000.00)
greg.printMe()
print(greg.salary)


#zac=greg.friend("Zac")
#print(zac.salary) #This gives error that 'Student' has no attribute salary

#So we use staticmethod
zac=WorkingStudent.friend_classMethod(greg, "Zac")
print(zac.salary)
zac.printMe() #Works, but how to pass salary for zac
