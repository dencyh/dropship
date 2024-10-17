# Drop Off 2.0

### ПО, которое требуется для запуска
python3, pip (идет в комплекте с python)
### Подготовка
1. Открыть терминал и перейти в папку с проектом
2. Выполнить:
   1. `python -m venv .venv`
   2. `.venv\Scripts\activate (Windows) / source .venv/bin/activate (Mac/Linux)`
   3. `pip install -r requirements.txt`

### Использование
1. Находясь в корне проекта активировать виртуальную среду командой `.venv\Scripts\activate` (если еще не активирована)
2. Положить 2 секретных файлика в input_data
3. Запустить командой `python src/main.py`
4. Забрать готовый `result.xlx` в корневой директории


### Собрать исполняемый файл
1. Открыть терминал и перейти в папку с проектом
2. Проделать шаги из раздела **Подготовка** выше
3. Выполнить команду `pyinstaller --onefile --add-data "config.yaml:." --add-data "input_data:input_data" src/main.py`

В результате команды получаем папки `build` и `dist`. В папке `dist` находится исполняемый файл `main`.
Для корректной работы рядом с папкой `dist` должна находиться папка `input_data`, где должны будут лежать данные для сборки