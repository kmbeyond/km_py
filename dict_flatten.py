
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

l1 = [x for x in dict_flat.items()]
import pandas as pd
df = pd.DataFrame(l1)
df.columns = ['element', 'value']
print(df)


#--------full flattening

def flatten_full(y):
  out = {}

  def flatten(x, name=''):
    if type(x) is dict:
      for a in x:
        flatten(x[a], name + a + '.')
    elif type(x) is list:
      i = 0
      for a in x:
        flatten(a, name + str(i) + '.')
        i += 1
    else:
      out[name[:-1]] = x

  flatten(y)
  return out


d_flat2 = flatten_full(d)
l1 = [x for x in d_flat2.items()]

df = pd.DataFrame(l1)
df.columns = ['element', 'value']
print(df)
