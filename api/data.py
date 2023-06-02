import pandas as pd

def load_data(file_path):
    """
    Загрузка данных из файла CSV.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None

def filter_and_sort_data(data, filters=None, sort_by=None):
    """
    Применение фильтров и сортировки к данным.
    """
    if filters:
        for filter_str in filters:
            column, value = filter_str.split(':')
            data = data[data[column] == value]

    if sort_by:
        sort_columns = sort_by.split(',')
        data = data.sort_values(by=sort_columns)

    return data.to_json(orient='records')
