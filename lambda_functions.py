

#lambda to square a number

print(lambda: 4*2)
#=> 8

my_lambda = lambda x: x*2
#The above is same as:  def my_lambda(x): return x*2

print(my_lambda(5))

#one liner of above function
print((lambda x: x*2)(5))


#apply lambdas on collections

#---on list
my_list = [2,4,6]
list_squared = list(map(my_lambda, my_list))
print(list_squared)

#---on Dict
my_dict = {"name": "kevin", "sal": 100000}
dict_squared1 = my_dict.copy()
dict_squared1['sal']=my_lambda(dict_squared1['sal'])
print(dict_squared1)
print(my_dict)

#---on Dict: redefine lambda & map()
my_lambda2 = lambda x,sal: { y=x.copy(); y[sal]=my_lambda(x[sal]); y }
dict_squared2 = my_lambda2(my_dict, 'sal')
print(dict_squared2)


#import toolz
#dict_squared2 = toolz.valmap(my_lambda, my_dict)
#print(dict_squared2)

