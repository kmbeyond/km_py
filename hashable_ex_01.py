#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:42:03 2017

@author: kiran
"""
class Hero:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + str(self.age)

    def __hash__(self):
        print(hash(str(self)))
        return hash(str(self))

    def __eq__(self,other):
        return self.name == other.name and self.age== other.age




heroes = set()
heroes.add(Hero('Zina Portnova', 16)) # gets hash
print(len(heroes)) # gets 1
print("hero: id= {}".format( id(Hero('Zina Portnova', 16))) )

heroes.add(Hero('Lara Miheenko', 17)) # gets hash -2822451113328084695
print(len(heroes)) # gets 2
print(id(heroes))
heroes.add(Hero('Zina Portnova', 16)) # gets hash -8926039986155829407
print(len(heroes)) # gets 2
print("hero: id= {}".format( id(Hero('Zina Portnova', 16))) )


h1 = Hero('Zina Portnova', 16)
print("Hero instance: id= {}; hash: {}".format( id(h1), hash(h1) ))

print("----- Add Plain/Non-Hashable class to Set")
class NonHashable:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} : {}".format(self.name, self.age)

    def __hash__(self):
        print("Hash: {}".format(hash(str(self))) )
        return hash(str(self))

    def __eq__(self,other):
        return self.name == other.name and self.age== other.age

nhSet = set()
nhSet.add( NonHashable("Jack", 10)) #1
nhSet.add( NonHashable("Jack", 10)) #2
print("id= {}".format( id(NonHashable("Jack", 10))) )
print("id= {}".format( id(NonHashable("Jack", 10))) )
print(len(nhSet) ) #returns 2; But it should return 1 because both are same


print("------ Use String object as key")
setStr = set()
print("set id()= {}".format( id(setStr)) )
print("str id= {}; hash: {}".format( id("AAA"), hash("AAA") ))
setStr.add("AAA")

print("set id()= {}".format( id(setStr)) ) #id() & hash() remain same
print("str id= {}; hash: {}".format( id("AAA"), hash("AAA") )) #This string has same hash, so can't add duplicate key in Set
setStr.add("AAA")

print("set id()= {}".format( id(setStr)) )

print(len(setStr)) #1: single item added due to String hash is same


print("--------- Strings are immutable, so id changes for value changes")
str="Kiran"
print("id= {}; hash: {}".format( id(str), hash(str) ))

str="Kiran2"
print("id= {}; hash: {}".format( id(str), hash(str) ))