CATEGORIES = {
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



ARCHIVE_EXT_TO_ARGUMENT = {
    ".zip": "zip",
    ".gz": "gztar",
    ".tar": "tar",
}



TRANSLIT_VOCAB = {
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