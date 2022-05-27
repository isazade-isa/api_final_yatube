### Описание:

API для социалной сети YaTube. Имеет следующие возможности: публиковать и комментировать записи, а так же подписываться или отписываться от авторов.

### Технологии:

Python 3.7, Django 2.2.16, DRF, JWT + Djoser

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:isazade-isa/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
Для Mac  ---  python3 -m venv venv
Для Win  ---  python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
