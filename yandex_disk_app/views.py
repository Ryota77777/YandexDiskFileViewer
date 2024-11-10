import io
from typing import List, Dict, Any
import requests
from flask import Response, render_template, request, send_file, Blueprint

views = Blueprint('views', __name__)

def get_files(public_key: str) -> Dict[str, Any]:
    url = "https://cloud-api.yandex.net/v1/disk/public/resources"
    params = {"public_key": public_key}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Проверка на наличие файлов
        if '_embedded' not in data:
            return {'files': [], 'error': 'Ключ не содержит доступных файлов или некорректен'}

        files = []
        for item in data.get('_embedded', {}).get('items', []):
            if item.get('type') == 'file':
                download_url_response = requests.get(
                    "https://cloud-api.yandex.net/v1/disk/public/resources/download",
                    params={"public_key": public_key, "path": item['path']}
                )
                download_url_response.raise_for_status()
                download_url = download_url_response.json().get("href")
                files.append({
                    'name': item.get('name'),  
                    'file_url': download_url,   
                    'type': item.get('mime_type', 'Неизвестный тип')  # Добавляем тип файла
                })
        return {'files': files, 'error': None}
    except requests.RequestException as e:
        print(f"Ошибка: {e}")
        return {'files': [], 'error': 'Некорректный публичный ключ или ошибка сети'}

@views.route("/", methods=["GET", "POST"])
def index():
    files = []
    error = None
    file_type_filter = request.form.get("file_type")  # Получаем выбранный тип файла
    if request.method == "POST":
        public_key = request.form.get("public_key")
        result = get_files(public_key)
        files = result['files']
        error = result['error']

        # Фильтрация файлов по типу
        if file_type_filter:
            files = [file for file in files if file_type_filter in file['type']]

    return render_template("index.html", files=files, error=error, file_type_filter=file_type_filter)

@views.route("/download")
def download():
    file_url = request.args.get("file_url")
    file_name = request.args.get("file_name")

    if not file_url or not file_name:
        return "URL или имя файла не переданы", 400
    try:
        response = requests.get(file_url, stream=True)
        response.raise_for_status()

        def generate():
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    yield chunk

        return Response(
            generate(),
            headers={
                'Content-Disposition': f'attachment; filename="{file_name}"',
                'Content-Type': response.headers.get('Content-Type', 'application/octet-stream')
            }
        )
    except requests.RequestException as e:
        return f"Ошибка при скачивании файла: {e}", 500







