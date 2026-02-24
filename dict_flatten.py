#-----------------Flatten Dictionary into base key-value pairs-------------


#---source data dictionary
data = { 'x': {'x1': 1, 'x2':[1.1,1.2], 'x3': {'x3_a': 1.333} }, 'y': {'y': 2, 'y2':[2.20, 2.21, 2.22]}, 'z': 3}

#--dictionary from file
json_path = '/Users/km/Downloads/70437492542209_run_results.json'
import json
data = json.load(open(json_path))

from pathlib import Path
json_path = Path(json_path)
with json_path.open("r", encoding="utf-8") as f:
    data = json.load(f)


#------------
from __future__ import annotations

import json
from typing import Any, Dict, Union
LeafValue = Union[str, int, float, bool, None]

def read_json_as_dot_kv(data: dict) -> Dict[str, LeafValue]:
    """
    Read a JSON dictionary and return a flattened dict of dot-separated keys -> leaf values.

    Rules:
    - Dictionaries are flattened: keys joined with "." (e.g., "a.b.c").
    - Lists are flattened: index is appended as "[i]" (e.g., "a.b[0].c").
    - Leaf values are primitives: string/number/bool/null.
    """

    out: Dict[str, LeafValue] = {}

    def walk(node: Any, prefix: str = "") -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                new_prefix = f"{prefix}.{k}" if prefix else str(k)
                walk(v, new_prefix)
        elif isinstance(node, list):
            for i, item in enumerate(node):
                new_prefix = f"{prefix}[{i}]" if prefix else f"[{i}]"
                walk(item, new_prefix)
        else:
            # primitive leaf (str/int/float/bool/None)
            out[prefix] = node

    walk(data, "")
    return out



#flatten
kv3 = read_json_as_dot_kv(data)

for k in kv3.items(): print(k[0],'--->', k[1])

#read into pandas dataframe
import pandas as pd
df = pd.DataFrame(kv3)
df.columns = ['element', 'value']
print(df)

