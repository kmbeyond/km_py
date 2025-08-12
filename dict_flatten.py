
d = { 'x': {'x1': 1, 'x2':[1.1,1.2], 'x3': {'x3_a': 1.333} }, 'y': {'y': 2, 'y2':[2.2,2.2,2.3]}, 'z': 3}


def flatten_dict(d, parent_key='', sep='_', used_keys=None):
    if used_keys is None:
        used_keys = set()
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        orig_key = new_key
        suffix = 1
        while new_key in used_keys:
            new_key = f"{orig_key}_{suffix}"
            suffix += 1
        used_keys.add(new_key)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep, used_keys=used_keys).items())
        else:
            items.append((new_key, v))
    return dict(items)


dict_flat = flatten_dict(d, parent_key='', sep='.', used_keys=None)

l1=[x for x in dict_flat.items()]
for x in l1: print(x[0],' = ', x[1])

import pandas as pd
df =pd.DataFrame(l1)
df.columns = ['element','value']
print(df)

