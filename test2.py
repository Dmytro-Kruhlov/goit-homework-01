import os
import shutil
from sort import normalize, categorize, get_extension, extract_archive

#def move_image(file_path):
    #file_name = os.path.basename(file_path)
    #category = categorize(file_name)

    #if category != 'unknown':
        #new_folder = os.path.join(os.path.dirname(file_path), category)

        #if os.path.exists(new_folder) and os.path.isdir(new_folder):
            #new_file_name = normalize(file_name)
            #destination = os.path.join(new_folder, new_file_name)
            #shutil.move(file_path, destination)
        #else:
            #os.makedirs(new_folder)
            #new_file_name = normalize(file_name)
            #destination = os.path.join(new_folder, new_file_name)
            #shutil.move(file_path, destination)


def move_archive(file_path):
    file_name = os.path.basename(file_path)
    name_without_extansion = os.path.splitext(file_name)[0]
    category = categorize(file_name)

    category_folder = os.path.join(os.path.dirname(file_path), category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    extraction_folder = os.path.join(category_folder, name_without_extansion)
    extract_archive(file_path, extraction_folder)

    normalized_name = normalize(name_without_extansion)
    new_folder_name = os.path.join(category_folder, normalized_name)
    os.rename(extraction_folder, new_folder_name)
    os.remove(file_path)


move_archive('F:\\test\\asvvte.zip')
