
#-----------------Flatten Dictionary into base key-value pairs-------------
#--2 methods:
#Method#1: Full flatten until string end value
#Method#2: breaks down only till list or String



#-----------------Method#1: Full flatten until string end value--------
#--returns list of key-value paurs
#--key: appended keys by dot
#--values: end data in string or list format

#--------------functions---------------
#---inner recursive function
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


def flatten_full_kv_pairs(d):
    d_flat2 = flatten_full(d)
    kv_pairs = [x for x in d_flat2.items()]
    return kv_pairs


#call function to flatten
kv2 = flatten_full_kv_pairs(data)
for k in kv2: print(k[0],'--->', k[1])

#read into pandas dataframe
import pandas as pd
df = pd.DataFrame(kv2)
df.columns = ['element', 'value']
print(df)





#------------------Method#2: breaks down only till list or String
#--Limitation: Does NOT break a list further into individul values (ex: if list contains a dict)

#---inner recursive function
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

def flatten_dict_kv_pairs(d):
    dict_flat = flatten_dict(d, parent_key='', sep='.', used_keys=None)
    kv_pairs = [x for x in dict_flat.items()]
    return kv_pairs

#-----------functions END-----------

#call function to flatten
kv = flatten_dict_kv_pairs(data)
for k in kv: print(k[0],'--->', k[1])

#read into pandas dataframe
import pandas as pd
df = pd.DataFrame(kv)
df.columns = ['element', 'value']
print(df)

