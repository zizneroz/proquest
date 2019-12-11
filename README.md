### Características

- Uso de DJango 2.2.7 y Python 3
- Manejo de archivos CSV
- Creacion de archivos .zip
- Conexión a un servidor remoto por medio de SSH
- Descarga de archivos PDF de servidor remoto
- Creacion de archivos XML
- Consulta, guardado y actualizacion de datos en SQLite3

# Proquest

<img src="https://migantoju.com/wp-content/uploads/2018/12/1_u_Jr6FozmyMCi3pe9ZsoFg-768x432.png"  width="384" height="216" />


**Contenido**

** **
##Iniciar el proyecto

###Comprobar versiones de python y django

Para verificar que se tiene instalado python, ejecutar:

` $ python --version`

DJango:

` $ django-admin --version`

###Crear base de datos

Antes de todo debemos de migrar nuestra base de datos, lo cual se hace con los siguientes comandos:

Si no tenemos los archivos de migracion debemos crearlos:
`$ python3 manage.py makemigrations`

Enseguida, ejecutaremos el comando para crear el modelo en la base:
`$ python3 manage.py migrate`

###Ejecutar el servidor
Para poder correr el servidor de DJango en desarrollo, necesitamos ubicarnos en la carpeta donde se encuentra clonado el proyecto y ejecutar el siguiente comando:
`$ python3 manage.py runserver localhost:8080`


###Links para descargar python y django

`<Python>` : <https://www.python.org/downloads/>

`<Django>` : <https://docs.djangoproject.com/en/3.0/topics/install/>
