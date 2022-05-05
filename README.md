# STORE
## Nazrakhmet Aikun
## DOCUMENTATION
http://localhost:8000/docs
## Installation

Clone repository
```sh
cd store
```

FIRST PART:
setup virtualenv and install requirements
```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
SECOND PART:
run makemigration and migrate
```sh
python manage.py makemigrations
python manage.py migrate
```

THIDRD PART:
setup predefined categories and subcategories
```sh
python category.py
python manage.py runserver
```