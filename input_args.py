#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:35:02 2017

@author: kiran
"""

print("Named arguments:")
def named_args(name, school):
    print("name {}, school {}".format(name, school))
    
named_args("Jeff", "MIT")
named_args(school="Cambridge", name="Scott")

print("Using multi args:")
def my_long_args(arg1, arg2, arg3,arg4):
    return arg1+arg2+arg3+arg4;

print(my_long_args(1,3,6,8))

print("Using list as input:")
def my_long_list(list_arg):
    return sum(list_arg)

print(my_long_list([1,3,6,8]))


print("Using dynamic args (*args):")
def my_long_dyn_args(*args):
    return (args)

print(my_long_dyn_args(1,3,6,8,9))

#**kwargs: 
print("Using keyword args (*kwargs):")
def my_long_dyn_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

print(my_long_dyn_kwargs(1,3,6,8,11, name="Jose", location="UK"))
