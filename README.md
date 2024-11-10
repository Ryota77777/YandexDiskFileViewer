# Просмотр и загрузка файлов с Яндекс.Диска

Этот проект представляет собой веб-приложение, которое позволяет пользователям получить доступ к файлам, размещённым на Яндекс.Диске, с использованием публичных ссылок. Пользователи могут ввести публичный ключ, выбрать тип файлов (например, изображения или документы) и просмотреть доступные файлы с возможностью их скачивания.

## Особенности

- **Ввод публичного ключа** — позволяет получить доступ к файлам по публичной ссылке.
- **Фильтрация файлов** — возможность выбрать тип файлов для отображения (изображения, документы и т.д.).
- **Просмотр файлов** — таблица с данными о файлах, включая их название, тип и доступную ссылку для скачивания.
- **Реализация на Python (Flask)** — серверная часть написана с использованием Flask для обработки запросов и отображения данных.
- **Гибкая структура UI** — форма поиска и таблица с результатами корректно отображаются как в вертикальной, так и в горизонтальной ориентации.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
2. Перейдите в папку проекта:
   ```bash
   cd yourrepository
3.Установите зависимости:
   ```bash
   pip install -r requirements.txt
4.Запустите приложение:
   ```bash
   python app.py
5.Перейдите в браузер по адресу: http://127.0.0.1:5000/ чтобы увидеть приложение.

Структура проекта
- app.py — основной файл приложения Flask.
- templates/ — папка, содержащая HTML-шаблоны.
- index.html — основной шаблон страницы.
- static/ — статические файлы (CSS, изображения, и т.д.).
- requirements.txt — файл с зависимостями для установки через pip.
Пример работы
При успешном запуске приложение будет отображать форму для ввода публичного ключа Яндекс.Диска и выбора типа файлов. После нажатия кнопки "Получить файлы", приложение загрузит список доступных файлов, отображая их названия и типы. Также будет предоставлена ссылка для скачивания каждого файла.

Пример интерфейса:
## Скриншот
![Скриншот](https://github.com/Ryota77777/YandexDiskFileViewer/blob/main/screen11.jpg?raw=true)
