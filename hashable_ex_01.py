#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:42:03 2018

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
heroes.add(Hero('Zina Portnova', 16)) # gets hash -8926039986155829407
print(len(heroes)) # gets 1

heroes.add(Hero('Lara Miheenko', 17)) # gets hash -2822451113328084695
print(len(heroes)) # gets 2

heroes.add(Hero('Zina Portnova', 16)) # gets hash -8926039986155829407
print(len(heroes)) # gets 2 
