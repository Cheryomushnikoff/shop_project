## Интернет-магазин

1. Установить виртуальное окружение
```
python -m venv .venv
```
2. Включить виртуальное окружение 
```
.venv\scripts\activate
```
3. Установить все зависимости, необходимые для работы проекта
```
pip install -r requirements.txt
```
4. Создать миграции
```
python manage.py makemigrations
```
5. Применить миграции
```
python manage.py migrate
```
7. Создать суперпользователя
```
python manage.py createsuperuser
```
6. Можно запускать сервер
```
 python manage.py runserver
```
