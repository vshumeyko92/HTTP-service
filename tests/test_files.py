import os
import pytest
from api.files import get_uploaded_files, delete_file

@pytest.fixture
def sample_files(tmpdir):
    # Создаем временные файлы для тестирования
    file1 = tmpdir.join("file1.txt")
    file1.write("Test File 1")

    file2 = tmpdir.join("file2.txt")
    file2.write("Test File 2")

    return [file1, file2]

def test_get_uploaded_files(sample_files):
    # Тест получения списка загруженных файлов
    files = get_uploaded_files()
    assert len(files) == 2
    assert "file1.txt" in files
    assert "file2.txt" in files

def test_delete_file(sample_files):
    # Тест удаления файла
    file_to_delete = sample_files[0]
    filename = file_to_delete.basename

    # Проверяем, что файл существует перед удалением
    assert os.path.exists(file_to_delete)

    # Удаляем файл
    deleted = delete_file(filename)
    assert deleted is True

    # Проверяем, что файл больше не существует
    assert not os.path.exists(file_to_delete)

    # Проверяем, что удаление несуществующего файла возвращает False
    deleted = delete_file(filename)
    assert deleted is False
