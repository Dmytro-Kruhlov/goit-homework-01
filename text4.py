def categorize_files(folder_path):
    file_paths = get_files_from_folder(folder_path)

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        category = categorize(file_name)
        normalized_name = normalize(file_name)
        new_folder = os.path.join(folder_path, category)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        new_file_path = os.path.join(new_folder, normalized_name)
        shutil.move(file_path, new_file_path)


def extract_archives(folder_path):
    extraction_folder = os.path.join(folder_path, 'archives')
    if not os.path.exists(extraction_folder):
        os.makedirs(extraction_folder)

    file_paths = get_files_from_folder(folder_path)

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        category = categorize(file_name)

        if category == 'archives':
            archive_name = os.path.splitext(file_name)[0]
            normalized_archive_name = normalize(archive_name)

            archive_folder = os.path.join(
                extraction_folder, normalized_archive_name)

            if not os.path.exists(archive_folder):
                os.makedirs(archive_folder)

            shutil.unpack_archive(file_path, archive_folder)
