
#read file directly into a string
file_entries = open('file_creation_in_bulk_names.txt')
contents = file_entries.read()
file_entries.close()


#file data
file_contents = """
select * from <<TABLE_NAME>>
"""

#create files
file_creation_path = "/home/km/km/km_practice/astronomer/dbt/km_test"

for line in contents.split('\n'):
    file_name = f"{file_creation_path}/km_{line}.sql"
    print(f"---> {line} --> {file_name}")
    file_contents_upd = file_contents.replace("<<TABLE_NAME>>", line)
    with open(file_name, 'w') as file:
        file.write(file_contents_upd)


