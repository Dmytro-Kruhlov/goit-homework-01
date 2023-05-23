import os
import shutil
import data

def extract_archive(archive_path: str, destination_folder: str):
    filename = os.path.basename(archive_path)
    _, extension = os.path.splitext(filename)

    shutil.unpack_archive(
        archive_path,
        destination_folder,
        data.ARCHIVE_EXT_TO_ARGUMENT[extension]
    )


def get_extension(filename: str) -> str:
    tokens = filename.split(".")
    return tokens[-1]


def get_files_from_folder(path: str) -> list:
    file_paths = []

    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
        else:
            file_paths += get_files_from_folder(file_path)
    return file_paths
    

def remove_empty_folders(path: str):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)