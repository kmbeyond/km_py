#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:35:02 2017

@author: kiran
"""

print("------- arguments---------------")
def named_args(name, school):
    print("name {}, school {}".format(name, school))
    
named_args("Jeff", "MIT")
named_args(school="Cambridge", name="Scott")


print("Using multi args:")
def my_long_args(arg1, arg2, arg3,arg4):
    print("arg1={}, arg2={}, arg3={}, arg4={}".format(arg1, arg2, arg3, arg4))
    return arg1+arg2+arg3+arg4;

print(my_long_args(1,2,3,4))

#Can change order if passing by name
print(my_long_args(arg2=2, arg1=1,arg4=4, arg3=3))

#if intend to pass None
def getName(name):
    if name:
        print("name= {}".format(name))
    else:
        print("Not passed")

getName("Kevin")

getName(None)


print("------- List as input-------------")
def my_long_list(list_arg):
    for indx in range(len(list_arg)):
        print("list_arg[{}] : {}".format(indx, list_arg[indx]))
    return sum(list_arg)

print(my_long_list([1,3,6,8]))



#args: dynamic args
print("---------- *args: dynamic args ------------")
def my_long_dyn_args(*args):
    #if(len(args) >= 1):
    #if (args.__len__() >= 1):
    if args:
        print("*args: {}".format(args))
        return (sum(args))
    else:
        print("*args: {}".format(args))
        return None

print(my_long_dyn_args(1,3,6,8,9))

print(my_long_dyn_args())


print("------------ **kwargs (keyword args; returns a dictionary)-------------")
def my_long_dyn_kwargs(**kwargs):
    #if (kwargs.__len__() >= 1):
    if kwargs:
        print("**kwargs: {}".format(kwargs))
        print("**kwargs[name]: {}".format(kwargs.get("name", "")))
        print("**kwargs[location]: {}".format(kwargs.get("location", None)))
    print("")

#Pass only kwargs
print("passing only kwargs:")
my_long_dyn_kwargs(name="Jack", location="UK", education="MS")

my_long_dyn_kwargs(name="Anthony")

sName="Amy"
my_long_dyn_kwargs(name=sName)


print("------------args & kwargs-------------")
#**kwargs: keyword args
print("Using keywords: *args & **kwargs:")
def my_long_dyn_args_kwargs(*args, **kwargs):
    #if(len(args) >= 1):
    #if (args.__len__() >= 1):
    if args:
        print("*args: {}".format(args))

    #if (kwargs.__len__() >= 1):
    if kwargs:
        print("**kwargs: {}".format(kwargs))
    print("")

#Pass only args
print("passing only args:")
my_long_dyn_args_kwargs(1,3,6,8,11, None)
my_long_dyn_args_kwargs(None)

#Pass only kwargs
print("passing only kwargs:")
my_long_dyn_args_kwargs(name="Jack", location="UK")

#Pass args & kwargs
print("passing both args & kwargs:")
my_long_dyn_args_kwargs(1,3,6,8,11, name="Jack", location="UK")








