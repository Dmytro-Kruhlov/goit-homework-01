import os
import shutil
categories = {
    'jpeg': 'images',
    'png': 'images',
    'jpg': 'images',
    'svg': 'images',
    'avi': 'video',
    'mp4': 'video',
    'mov': 'video',
    'mkv': 'video',
    'doc': 'documents',
    'docx': 'documents',
    'txt': 'documents',
    'pdf': 'documents',
    'xlsx': 'documents',
    'pptx': 'documents',
    'ogg': 'audio',
    'mp3': 'audio',
    'wav': 'audio',
    'amr': 'audio',
    'zip': 'archives',
    'gz': 'archives',
    'tar': 'archives'
}


def extract_archive(archive_path, destination_folder):
    filename = os.path.basename(archive_path)
    _, extension = os.path.splitext(filename)

    if extension == '.zip':
        shutil.unpack_archive(archive_path, destination_folder, 'zip')
    elif extension == '.gz':
        shutil.unpack_archive(archive_path, destination_folder, 'gztar')
    elif extension == '.tar':
        shutil.unpack_archive(archive_path, destination_folder, 'tar')



def get_extension(filename: str) -> str:
    tokens = filename.split(".")
    return tokens[-1]




def categorize(filename: str) -> str:
    #filename = 'face.jpeg'
    extension = get_extension(filename)
    category = categories.get(extension, 'unknown')
    return category



def get_files_from_folder(path):
    file_paths = []

    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
        else:
            file_paths += get_files_from_folder(file_path)
    return file_paths
    



def normalize(name: str) -> str:
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh',
        'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts',
        'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu',
        'Я': 'Ya'
    }

    normalized_name = ''
    for char in name:
        if char.isalpha():
            if char in translit_dict:
                normalized_name += translit_dict[char]
            else:
                normalized_name += char
        elif char.isdigit() or char == ".":
            normalized_name += char
        else:
            normalized_name += '_'

    return normalized_name   




def move_files(file_path):
    file_name = os.path.basename(file_path)
    category = categorize(file_name)

    new_folder = os.path.join(os.path.dirname(file_path), category)

    if os.path.exists(new_folder) and os.path.isdir(new_folder):
        new_file_name = normalize(file_name)
        destination = os.path.join(new_folder, new_file_name)
        shutil.move(file_path, destination)
    else:
        os.makedirs(new_folder)
        new_file_name = normalize(file_name)
        destination = os.path.join(new_folder, new_file_name)
        shutil.move(file_path, destination)



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


def move_files_from_subfolders(path):
    
    file_paths = get_files_from_folder(path)
    moved_file = []
    
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        destination = os.path.join(path, file_name)
        shutil.move(file_path, destination)
        moved_file.append(destination)
    return moved_file



def remove_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)






def categorize_files (files_list):

    category_files = {
        'images': [],
        'video': [],
        'documents': [],
        'audio': [],
        'archives': []
    }

    all_extensions = set()
    unknown_extensions = set()

    for file_path in files_list:
        file_extension = os.path.splitext(file_path)[1][1:].lower()
        all_extensions.add(file_extension)

        category = categories.get(file_extension, 'unknown')
        if category != 'unknown':
            category_files[category].append(file_path)
        else:
            unknown_extensions.add(file_extension)

    return category_files, all_extensions, unknown_extensions


def sorter(path_to_folder):
    
    file_paths = move_files_from_subfolders(path_to_folder)
    print(categorize_files(file_paths))
    for path in file_paths:
        if path.endswith('.zip') or path.endswith('.gz') or path.endswith('.tar'):
            move_archive(path)
            
        else:
            move_files(path)
            
    remove_empty_folders(path_to_folder)