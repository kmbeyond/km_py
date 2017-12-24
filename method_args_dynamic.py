

# args are a tuple
# kwargs is a dictionary

#-----------------------------args--------------------------------
def print_all_args(*args):
    print("Args count: {}".format(len(args)))
    print(args)
    for l in range(len(args)):
        print("args {}: {}".format(l, args[l]))


print_all_args(899, 44, 32)


print_all_args(12, 35, 64, 'hello')



#-----------------------------kwargs--------------------------------
def print_kwargs(**kwargs):
    print("kwargs: {}".format(kwargs))
    for key in kwargs.keys():
        print("args {}: {}".format(key, kwargs[key]))



print_kwargs(fname='Kiran', location='Peoria')
print_kwargs(fname='Kiran', location='Peoria')


#-----------------------------args & kwargs--------------------------------
# As well as a tuple of args, we can pass kwargs

def print_args_kwargs(*args, **kwargs):
    print("args: {}".format(args))
    print("kwargs: {}".format(kwargs))

print_args_kwargs(name='Jack', location='Peoria')
print_args_kwargs(323, 55, 77, name='Jane', location='Seattle')
