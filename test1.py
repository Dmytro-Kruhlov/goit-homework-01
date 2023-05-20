import os
def get_files_from_folder(path):
    #files = os.listdir(path)
    #return files
    #files = os.listdir(path)
    #file_paths = [os.path.join(path, file) for file in files if os.path.isfile(os.path.join(path, file))]
    file_paths = []

    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
        else:
            file_paths += get_files_from_folder(file_path)
    return file_paths
print(get_files_from_folder("F:\\test"))
    

