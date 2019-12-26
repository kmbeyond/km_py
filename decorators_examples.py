#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 06:40:50 2017

@author: kiran
"""

import functools


#---------------------
#decorator
def my_decorator_no_args(func):
    @functools.wraps(func)
    def run_function():
        print("function calling..")
        func()
        print("function completed")
    return run_function
    
@my_decorator_no_args
def my_function_no_args():
    print("I'm real function with no args")

    
my_function_no_args()
'''Output:
function calling..
I'm real function with no args
function completed
'''

#---------------------

def my_decorator_with_args(name):
    def my_decorator(func):
        @functools.wraps(func)
        def run_function(name):
            print("function calling..")
            if name.upper()=="ADMIN":
                func(name)
            else:
                print("Can't call function for nonadmins")
            print("function completed")
        return run_function
    return my_decorator

@my_decorator_with_args("AAA")
def my_function_with_args(name):
    print("I'm real function called by {}".format(name))
 
my_function_with_args("admin")


#---------------------


def my_decorator_with_dyn_args(name):
    def my_decorator(func):
        @functools.wraps(func)
        def run_function(name, *args, **kwargs):
            print("function calling..")
            if name.upper()=="ADMIN":
                func(name, *args, **kwargs)
            else:
                print("Can't call function for nonadmins")
            print("function completed")
        return run_function
    return my_decorator

@my_decorator_with_dyn_args("AAA")
def my_function_with_dyn_args(name, x,y):
    print("I'm real function called by {} to sum {}".format(name, x+y))
 
my_function_with_dyn_args("admin", 10, 20)





