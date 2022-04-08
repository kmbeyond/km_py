

def compress_file(stage_path, file_name, target_path, target_file_name):
    import gzip
    with open(stage_path+file_name, 'rb') as f_in, gzip.open(target_path+target_file_name, 'wb') as f_out:
        f_out.writelines(f_in)
    f_out.close()
    f_in.close()
    #os.unlink(stage_path+file_name)

def decompress_file(stage_path, file_name, target_path, target_file_name):
    import gzip, shutil
    with gzip.open(stage_path+file_name, "rb") as f_in, open(stage_path+target_file_name, "wb") as f_out:
        f_out.write(f_in.read())
        #shutil.copyfileobj(f_in, f_out)
    f_out.close()
    f_in.close()

    
#create a simple file
str_data = "line1\nline2\nline3"
file_name = "zz_test.txt"
with open(file_name, 'w') as file:
    file.write(f"{str_data}")

#--compress to gz file
compress_file("", file_name, "", file_name+".gz")

#--decompress it as BKP file
decompress_file("", file_name+".gz", "", file_name+"_BKP")

