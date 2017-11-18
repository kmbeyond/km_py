#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 06:18:41 2017

@author: kiran
"""

def callMethod(another):
    return another()


def add_two_num():
    return 3+7


print(callMethod(add_two_num))


#lambda functions
print((lambda x: x*2)(7))
# => 14
#The above is same as:
def f(x):
    return x*2

f(5)


print(callMethod(lambda: 4+8))
#=> 12

#Print even numbers from List
my_list=[11,44,33,66,88,99]

#using list operation
print([x for x in my_list if x%2==0])

#using lambda
print(list(filter(lambda x: x%2==0, my_list)))

#using filter()
def not_even(x):
    return x if x%2==0 else None

print(list(filter(not_even, my_list)))





