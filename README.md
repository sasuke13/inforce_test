You need to change your settings of database in Restaurant/Restaurant/settings, where you should find DATABASES dict and change db options on your own

before running server you should type in terminal next command: "python Restaurants/manage.py migrate" to migrate everything to your postgres db

finnaly, to run server you should type in terminal next command: "python Restaurants/manage.py runserver"
