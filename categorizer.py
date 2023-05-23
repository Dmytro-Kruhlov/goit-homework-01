import os
import data
import utils


def categorize(filename: str) -> str:
   
    extension = utils.get_extension(filename)
    category = data.CATEGORIES.get(extension, 'unknown')
    return category


def categorize_files (files_list: list):

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
        

        category = data.CATEGORIES.get(file_extension, 'unknown')
        if category != 'unknown':
            category_files[category].append(file_path)
            all_extensions.add(file_extension)
        else:
            unknown_extensions.add(file_extension)

    return {
        'to_move': category_files,
        'all_extensions': all_extensions,
        'unknown_extensions': unknown_extensions
    }