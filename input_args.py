#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:35:02 2017

@author: kiran
"""

def named_args(name, school="N/A-Not provided"):
    print("arguments: Name={}; School={}".format(name, school))
    if name:
        if 'N/A' not in school:
            print("Welcome {} to {}".format(name, school))
    else:
        print("Name is NOT passed")

named_args("Jeff", "MIT")
named_args(name="Scott", school="Cambridge")
named_args(name="Adam")
named_args(None)

# Can change order if passing by name
named_args(school="MIT", name="Bret")


print("---------- *args: variable/dynamic args ------------")
def get_sum(*args):
    print("*args: {}".format(args))
    # if(len(args) >= 1):
    # if (args.__len__() >= 1):
    if args:
        num_list = [int(itm) for itm in args if str(itm).isdigit()]
        return f"Total={sum(num_list)}"
    else:
        return None

print(f"get_sum()={get_sum(2,4,6,8)}")
print(f"get_sum()={get_sum(2,4,'a')}")
print(f"get_sum()={get_sum()}")


print("------------ **kwargs (keyword args; returns a dictionary)-------------")

def my_long_dyn_kwargs(**kwargs):
    print("*kwargs: {}".format(kwargs))
    # if (kwargs.__len__() >= 1):
    if kwargs:
        print("**kwargs[name]: {}".format(kwargs.get("name", "")))
        print("**kwargs[location]: {}".format(kwargs.get("location", None)))
    print("")


print("passing only kwargs:")
my_long_dyn_kwargs(name="Jack", location="UK", education="MS")

my_long_dyn_kwargs(name="Anthony")

sName = "Amy"
my_long_dyn_kwargs(name=sName)

mykwargs = {"name": "Jill", "location": "NJ", "education": "MS"}
my_long_dyn_kwargs(**mykwargs)

print("------------args & kwargs-------------")
# **kwargs: keyword args

def my_long_dyn_args_kwargs(*args, **kwargs):
    print("*args: {}".format(args))
    print("**kwargs: {}".format(kwargs))
    # if(len(args) >= 1):
    # if (args.__len__() >= 1):
    if args:
        print("-> args passed: {}".format(args))

    # if (kwargs.__len__() >= 1):
    if kwargs:
        print("-> kwargs passed: {}".format(kwargs))
    print("")


# Pass only args
print("passing only args:")
my_long_dyn_args_kwargs(1, 3, 6, 8, 11, None)
my_long_dyn_args_kwargs(None)

# Pass only kwargs
print("passing only kwargs:")
my_long_dyn_args_kwargs(name="Jack", location="UK")

# Pass args & kwargs
print("passing both args & kwargs:")
my_long_dyn_args_kwargs(1, 3, 6, 8, 11, name="Jack", location="UK")

