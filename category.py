import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

categories = [
    {
        "category":  "Автотовары",
        "subcategory" : [
            "Антифризы",
            "Электромотоциклы",
            "Электроскутеры",
            "Скутеры",
            "Трансмиссионные масла",
            "Моторные масла",
            "Мотоциклы",
            "Тормозные жидкости"
        ]
    },
    {
        "category":  "Одежда",
        "subcategory" : [
            "Обувь",
            "Одежда",
        ]
    },
    {
        "category":  "Телефоны и гаджеты",
        "subcategory" : [
            "Антифризы",
            "Электромотоциклы",
            "Электроскутеры",
            "Скутеры",
            "Трансмиссионные масла",
            "Моторные масла",
            "Мотоциклы",
            "Тормозные жидкости"
        ]
    },
    {
        "category":  "Телефоны и гаджеты",
        "subcategory" : [
            "Зарядное устройство",
            "Кабели и переходники для смартфонов",
            "Смартфоны",
            "Смарт-часы",
            "Системы нагревания  табака",
        ]
    }
]

from products.models import Category,Subcategory



for category in categories:
    cat = Category.objects.create(name=category.get('category'))
    for subcategory in category.get('subcategory'):
        Subcategory.objects.create(name=subcategory,category=cat)