import pytest
from api.data import load_data, filter_and_sort_data

@pytest.fixture
def sample_data():
    # Пример данных для тестирования
    data = [
        {"name": "John", "age": 25, "city": "New York"},
        {"name": "Alice", "age": 30, "city": "San Francisco"},
        {"name": "Bob", "age": 35, "city": "Chicago"},
    ]
    return data

def test_load_data(sample_data):
    # Тест загрузки данных
    data = load_data(sample_data)
    assert len(data) == 3

def test_filter_and_sort_data(sample_data):
    # Тест фильтрации и сортировки данных
    data = load_data(sample_data)

    # Применение фильтрации по столбцу "age"
    filters = ["age:30"]
    filtered_data = filter_and_sort_data(data, filters=filters)
    assert len(filtered_data) == 1
    assert filtered_data[0]["name"] == "Alice"

    # Применение сортировки по столбцу "name"
    sort_by = "name"
    sorted_data = filter_and_sort_data(data, sort_by=sort_by)
    assert len(sorted_data) == 3
    assert sorted_data[0]["name"] == "Alice"
    assert sorted_data[1]["name"] == "Bob"
    assert sorted_data[2]["name"] == "John"
