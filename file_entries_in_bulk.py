
#read file directly into a string
file_entries = open('file_creation_in_bulk_names.txt')
contents = file_entries.read()
file_entries.close()


#file data
file_contents = """,
 {
   "destination": "<<TABLE_NAME>>"
 }
"""

#create files
file_creation_path = "/home/km/km/km_practice/astronomer/config"
file_name = f"{file_creation_path}/config_file.json"

with open(file_name, 'a') as file:
    for line in contents.split('\n'):
        print(f"---> {line} --> {file_name}")
        file_contents_upd = file_contents.replace("<<TABLE_NAME>>", line)
        file.write(file_contents_upd)

file.close()
