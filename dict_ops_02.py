#Get dct item of max of specific key from dict
dataset = [{'country': 'Afghanistan',
     'continent': 'Asia',
     '1990': 500,
     '1991': 500,
     '1992': 500,
     '1993': 1000},
    {'country': 'Albania',
    'continent': 'Europe',
    '1990': 100,
    '1991': 100,
    '1992': 100,
    '1993': 100},
    {'country': 'Algeria',
    'continent': 'Africa',
    '1990': 500,
    '1991': 500,
    '1992': 1000,
    '1993': 1000
    }]
#Method#1:max(lambda)
max_dict = max(dataset, key=lambda x: x["1991"])
new_dict = {'country':max_dict['country'], 'year':1991, 'cases':max_dict['1991']}
print(new_dict)

#Method#2: iterate through dict
max_cntry=""
max_1991=0
for itm in dataset:
    if itm['1991'] > max_1991:
        max_1991 = itm['1991']
        max_cntry = itm['country']

    #print(f'*{itm}')
    #print(f"---> {itm['country']}")

new_dict={'country':max_cntry, 'year':1991, 'cases':max_1991}
print(new_dict)