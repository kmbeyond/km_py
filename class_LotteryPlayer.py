#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:47:18 2017

@author: kiran
"""

class LotteryPlayer:
    def __init__(self, name):
        self.name=name,
        self.numbers=(5,6,3,8)

    def total(self):
        return sum(self.numbers)

    def __str__(self):
        return "name= {}; numbers= {}".format(self.name, self.numbers)

#Create instance(s) of class
print("player1:")
player1=LotteryPlayer("John")
print(player1)

print("Name: "+str(player1.name))
print(player1.numbers)
player1.numbers = (1,3,5)
print(player1.numbers)

print("Total: "+str(player1.total()))



print("player2:")
player2=LotteryPlayer("Mike")

print(player1.name == player2.name)
