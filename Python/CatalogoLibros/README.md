# Catálogo de Libros

Éste un proyecto sencillo para aprender a realizar aplicaciones con una interfaz grafica usando Tkinter, para poder visualizarlo debes descargar el archivo o clonar el repositorio, posterior a ello buscar el fichero a traves de la terminal y ejecutarlo como cualquier archivo .py

En mi escritorio ya tengo el ejecutable hecho con pip installer, los pasos a seguir para ello fueron los siguientes:
1- Tener el entorno virtual activado y estar dentro de éste.
2- Ingresar [ `pip install pyinstaller` ] en la terminal
3- Ya que nuestro programa tiene muchas carpetas, pero sobre todo archivos como imagenes y una “base de datos” no podemos hacer un ejecutable así no'mas, debemos hacer algo antes:
 -Ingresamos [ `pyi-makespec catalogolibros.py --windowed` ] en la terminal.
 -Una vez que finalice su proceso veremos que se nos ha creado un archivo [ `.spec` ], éste archivo tiene toda la configuración necesaria para el ejecutable, debemos ingresar a él y en el apartado { datas=[] } debemos ingresar lo siguiente:
 -`datas=[('./img/*.ico', 'img'),('./database/*.db', 'database')]`
 -Se le esta indicando el fichero y que de ahí tome todos los archivos [ `.ico`], y que éstos debe de copiarlos en una carpeta llamada [ `img` ], lo mismo para el [ `.db` ]
4- Ahora vamos a poner [ `py installer catalogolibros.spec` ], al ejecutarlo se hará una serie de procesos que nos dará una carpeta [ `build y dist` ], ya solo es ir a la carpeta [ `dist` ] y buscar la aplicación

Ha sido bastante curioso dentro de la sencillez del proyecto, pero lo más importante es que me hace ver la importancia y profundidad que tiene la Programacion Oreintada a Objetos
