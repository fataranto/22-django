Ayuda

$ python manage.py --help



inicializar el server

$ python manage.py runserver



Crear una app (desde la carpeta del proyecto)

$ python manage.py startapp nombreApp 


Generar o modificar tablas en la base de datos sqlite

1)generar las migraciones
$ python manage.py makemigrations

2)aplicar la migración generada (nombre app + número de la migración generada). Esto genera el código SQL
$ python manage.py sqlmigrate nombreApp 0001

3)aplicar los cambios a la base de datos
$ python manage.py migrate