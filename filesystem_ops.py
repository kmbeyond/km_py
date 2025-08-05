import os
from pathlib import Path

for itm in Path.iterdir(Path.cwd()):
    print(f"File:{itm}")

search_path = '/Users/km/km_practice/data'

for itm in os.listdir(search_path):
    print(f"File:{itm}")

files_list = [file_name for file_name in os.listdir(search_path) if 'KM_DATA' in file_name]

len(files_list)
