import os
import shutil
from sort import get_files_from_folder, move_files, move_archive, move_files_from_subfolders, remove_empty_folders, categorize_files


def sorter(path_to_folder):

    
    file_paths = move_files_from_subfolders(path_to_folder)
    print(categorize_files(file_paths))
    for path in file_paths:
        if path.endswith('.zip') or path.endswith('.gz') or path.endswith('.tar'):
            move_archive(path)
        else:
            move_files(path)

    remove_empty_folders(path_to_folder)


sorter('F:\\test')