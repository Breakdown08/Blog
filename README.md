# Blog
 Репозиторий проверки лабораторной работы по промышленному программированию

Тема: Создание блога с использованием backend фреймворка Django

Дизайн и шаблоны страниц заимствованы: https://github.com/learning-zone/website-templates/
в образовательных целях

Порядок запуска проекта:

1) Клонировать репозиторий в удобное на компьютере место
2) Открыть проект в PyCharm
3) Убедиться в наличии установленной python библиотеки в ваш главный интерпретатор **pipenv**
4) (В случае отсутствия pipenv ввести команду в терминале: **pip install pipenv**)
5) В терминале ввести поочередно команды: <br> **pipenv shell** <br>
**pipenv sync** <br>
**pipenv update**
6) Сделать миграции в базу данных командой в терминале: **python manage.py migrate**
7) Запустить приложение командой в терминале: **python manage.py runserver**

