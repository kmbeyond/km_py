
import os
#os Functions
#https://docs.python.org/2/library/os.html

curr_dir = os.getcwd()
print(f"cwd: {curr_dir}")


#list of files in current dir
#from os import listdir
files_list = os.listdir(os.getcwd())
print(f"Listdir: {files_list}")


#Get directories, subdirectories & files
def get_dir_contents(s_path, files_list, list_sub_dir_flag):
    import os
    for s_item in os.listdir(s_path):
        s_item = os.path.join(s_path, s_item)
        if os.path.isdir(s_item):
            files_list.append(f'd - {s_item}')
            if list_sub_dir_flag: get_dir_contents(s_item, files_list, list_sub_dir_flag)
        else:
            files_list.append(f'f - {s_item}')

files_list = []
#get_dir_contents(os.getcwd(), files_list, list_sub_dir_flag=True)
for file in files_list:
    print(f" ---> {file}")




#---more customized - show only path after input path
def get_dir_contents_2(s_path, files_list, list_sub_dir_flag, hide_original_path):
    import os
    for s_item in os.listdir(s_path):
        s_item = os.path.join(s_path, s_item)
        if os.path.isdir(s_item):
            files_list.append(f'd - {s_item}'.replace(hide_original_path, ''))
            if list_sub_dir_flag: get_dir_contents_2(s_item, files_list, list_sub_dir_flag, hide_original_path)
        else:
            files_list.append(f'f - {s_item}'.replace(hide_original_path, ''))


#view dir, files & inside sub-dir
files_list2 = []
get_dir_contents_2(os.getcwd(), files_list2, list_sub_dir_flag=False, hide_original_path=os.getcwd())
for file in files_list2:
    print(f" ---> {file}")


#view only files (files inside subdir)
files_only_list2 = []
#get_dir_contents_2(os.getcwd(), files_only_list2, list_sub_dir_flag=False, hide_original_path=os.getcwd())
for file in files_only_list2:
    print(f" ---> {file}")



