## Установка проекта

Перейдите в папку:

``````
cd orders
``````

Необходимо создать и активировать виртуальное окружение.

``````
python3 -m venv env
``````

``````
source env/bin/activate
``````

Установите зависимости из файла **requirements.txt**:

``````
pip install -r requirements.txt
``````

В проекте есть предустановленная база данных sqlite

### Для создания новой базы данных необходимо сделать следующие шаги:

``````
python manage.py makemigrations
``````

``````
python manage.py migrate
``````

## Создание суперпользователя для Django-admin

По умолчанию установлен пользователь:

login:admin@gmail.com

password:admin1990

Создание нового супер пользователя:

``````
python manage.py createsuperuser
``````

* Команда для запуска приложения

``````
python manage.py runserver
``````
