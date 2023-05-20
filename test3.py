import os
import shutil




def extract_archive(archive_path, destination_folder):
    filename = os.path.basename(archive_path)
    _, extension = os.path.splitext(filename)

    if extension == '.zip':
        shutil.unpack_archive(archive_path, destination_folder, 'zip')
    elif extension == '.gz':
        shutil.unpack_archive(archive_path, destination_folder, 'gzip')
    elif extension == '.tar':
        shutil.unpack_archive(archive_path, destination_folder, 'tar')


extract_archive('F:\\test\\fmlfoi.m.zip', 'F:\\test')
