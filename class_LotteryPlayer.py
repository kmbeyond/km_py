#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:47:18 2017

@author: kiran
"""

class LotteryPlayer:
    play_limit=1000 #class attribute
    def __init__(self, name):
        self.name=name,
        self.numbers=(5,6,3,8)
        #self.play_limit=1500

    def total(self):
        return sum(self.numbers)

    def __str__(self):
        return "name= {}; numbers= {}; date={}".format(self.name, self.numbers, self.play_limit)

#Create instance(s) of class
print("player1:")
player1=LotteryPlayer("John")
print(player1)

print("--- class variable---")
print(LotteryPlayer.play_limit)

print("--- instance variable---")
print(player1.play_limit)

print("--- LotteryPlayer.play_limit=2000")
LotteryPlayer.play_limit=2000

print("--- class variable---")
print(LotteryPlayer.play_limit)

print("--- instance variable---")
print(player1.play_limit)

print("--- player1.play_limit=3000")
player1.play_limit=3000

print("--- class variable---")
print(LotteryPlayer.play_limit)

print("--- instance variable---")
print(player1.play_limit)


print("Name: {}".format(player1.name))
print(player1.numbers)
player1.numbers = (1,3,5)
print(player1.numbers)

print("Total: "+str(player1.total()))



print("player2:")
player2=LotteryPlayer("Mike")
print(player2)

print(player1.name == player2.name)


print("--- class variable---")
print(LotteryPlayer.play_limit)

print("--- instance variable---")
print(player2.play_limit)