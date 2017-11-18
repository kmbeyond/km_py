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
        return cls(name, origin.school, [])
    
    
anna = Student("Anna", "MIT", [60])
print(anna.marks)
anna.marks.append(80)
print(anna.marks)
anna.printMe()

print(anna.average())


anna.tellYourSchool()

#call classmethod
Student.tellYourSchool_classMethod()

#call staticmethod
Student.tellYourSchool_staticMethod()


andy=anna.friend("Andy")
andy.printMe()
andy.marks.append([60,90])
andy.printMe()



