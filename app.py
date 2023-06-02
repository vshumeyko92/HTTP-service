from flask import Flask, request, jsonify
from api.data import load_data, filter_and_sort_data
from api.files import get_uploaded_files, delete_file
from api.utils import allowed_file

app = Flask(__name__)

# Разрешенные расширения файлов
ALLOWED_EXTENSIONS = {'csv'}

@app.route('/upload', methods=['POST'])
def upload_file():
    # Проверка наличия файла в запросе
    if 'file' not in request.files:
        return jsonify({'error': 'No file found in request'}), 400

    file = request.files['file']

    # Проверка разрешенного расширения файла
    if not allowed_file(file.filename, ALLOWED_EXTENSIONS):
        return jsonify({'error': 'Invalid file extension'}), 400

    # Сохранение файла в директорию uploads
    file.save('uploads/' + file.filename)

    return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/files', methods=['GET'])
def get_files():
    # Получение списка загруженных файлов
    files = get_uploaded_files()
    return jsonify({'files': files}), 200

@app.route('/files/<filename>', methods=['DELETE'])
def delete_uploaded_file(filename):
    # Удаление загруженного файла
    deleted = delete_file(filename)

    if deleted:
        return jsonify({'message': f'File {filename} deleted successfully'}), 200
    else:
        return jsonify({'error': f'Failed to delete file {filename}'}), 404

@app.route('/data', methods=['GET'])
def get_data():
    # Получение данных из файла с фильтрацией и сортировкой
    filename = request.args.get('filename')
    filters = request.args.getlist('filters')
    sort_by = request.args.get('sort_by')

    # Загрузка данных из файла
    data = load_data('uploads/' + filename)

    if data is None:
        return jsonify({'error': f'Failed to load data from file {filename}'}), 404

    # Применение фильтров и сортировки к данным
    filtered_sorted_data = filter_and_sort_data(data, filters=filters, sort_by=sort_by)

    return filtered_sorted_data, 200

if __name__ == '__main__':
    app.run(debug=True)
