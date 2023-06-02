import os

def get_uploaded_files():
    """
    Получение списка загруженных файлов.
    """
    files = os.listdir('uploads')
    return files

def delete_file(filename):
    """
    Удаление загруженного файла.
    """
    file_path = os.path.join('uploads', filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False
