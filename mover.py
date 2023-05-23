import os
import shutil
import normalizer
import utils
import categorizer


def move_file(file_path: str, category: str):
    filename = os.path.basename(file_path)
    name_without_extension = os.path.splitext(filename)[0]
    new_folder = os.path.join(os.path.dirname(file_path), category)
    
    if  not (os.path.exists(new_folder) and os.path.isdir(new_folder)):
        os.makedirs(new_folder)
        
    new_file_name = normalizer.normalize(name_without_extension)
    print(new_file_name)
    destination = os.path.join(new_folder, f"{new_file_name}.{utils.get_extension(filename)}")
    
    shutil.move(file_path, destination)
    
def move_archive(file_path: str):
    filename = os.path.basename(file_path)
    name_without_extansion = os.path.splitext(filename)[0]
    category = categorizer.categorize(filename)

    category_folder = os.path.join(os.path.dirname(file_path), category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    extraction_folder = os.path.join(category_folder, name_without_extansion)
    utils.extract_archive(file_path, extraction_folder)

    normalized_name = normalizer.normalize(name_without_extansion)
    new_folder_name = os.path.join(category_folder, normalized_name)
    os.rename(extraction_folder, new_folder_name)    
    os.remove(file_path)


def move_files_from_subfolders(path: str) -> list:
    
    file_paths = utils.get_files_from_folder(path)
    moved_file = []
    
    for file_path in file_paths:
        filename = os.path.basename(file_path)
        destination = os.path.join(path, filename)
        shutil.move(file_path, destination)
        moved_file.append(destination)
    return moved_file