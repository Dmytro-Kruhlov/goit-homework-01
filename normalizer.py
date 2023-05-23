import data

def normalize(name: str) -> str:  # name - filename without extension
   
    normalized_name = ''
    for char in name:
        if char.isalpha():
            normalized_name += data.TRANSLIT_VOCAB.get(char, char)
            
        elif char.isdigit():
            normalized_name += char
        else:
            normalized_name += '_'

    return normalized_name   