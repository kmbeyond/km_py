
import os

#os Functions
#https://docs.python.org/2/library/os.html



#Print directories, subdirectories & files
def print_dir_iter_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            list_dir_contents(sChildPath)
        else:
            print("print_dir_iter_contents=", sChildPath)

def list_dir_contents(sPath):
    from os import listdir
    dirContents = [f for f in listdir(sPath)]
    return dirContents

def list_files(sPath):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(sPath) if isfile(join(sPath, f))]
    return onlyfiles


#Print files only
def print_files(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        print(sChildPath)
        if os.access(sChildPath, os.R_OK):
            try:
                with open(sChildPath) as fp:
                    print(fp.read())
            except IOError as e:
                if e.errno == errno.EACCES:
                    return "some default data"
                # Not a permission error.
                raise
            else:
                with fp:
                    return fp.read()


print("cwd: {}".format(os.getcwd()))
#print("terminal: {}".format(os.ctermid()))


files = list_files("/home/kiran")
#files = list_dir_contents("C:\\")
for f in files:
    print(f)

#print("-------------listdir-----------")
#print(os.listdir("/home/kiran"))

print_dir_iter_contents("/home/kiran")
#print_files("/home/kiran")


#print("login user: {}".format(os.getlogin()))
#print("PATH: {}".format(os.getenv("PATH")))


for k in sorted(dictEmp):
    print("Key={}; val={}".format(k, dictEmp[k]))
