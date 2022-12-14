from glob import glob

path = input()
file_paths = glob(path+"/"+"*.txt")
general = open(path+"/general.txt", "w")
for file_path in file_paths:
    file_name = file_path.split("/")[-1]
    general.write(file_name+":"+"\n")
    file = open(file_path, "r")
    general.writelines(file)
    file.close()
general.close()