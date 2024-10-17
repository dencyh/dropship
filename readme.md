# Drop Off 2.0

### ПО, которое требуется для запуска
python3, pip (идет в комплекте с python)
### Подготовка
1. Зайти в папку с проектом
2. Выполнить:
   1. `python -m venv .venv`
   2. `.venv\Scripts\activate (Windows) / source .venv/bin/activate (Mac/Linux)`
   3. `pip install -r requirements.txt`
### Использование
1. Находясь в корне проекта активировать виртуальную среду командой `.venv\Scripts\activate` (если еще не активирована)
2. Положить 2 секретных файлика в input_data
3. Запустить командой `python3 src/main.py`
4. Забрать готовый `result.xlx` в корневой директории