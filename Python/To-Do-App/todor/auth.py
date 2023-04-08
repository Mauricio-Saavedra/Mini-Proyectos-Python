from flask import (
	Blueprint, render_template, request, url_for, redirect, flash, session, g
)
from werkzeug.security import generate_password_hash, check_password_hash	#Importación de la función check_password_hash
from .models import User
from todor import db

# Creación del Blueprint
bp = Blueprint('auth', __name__, url_prefix = '/auth')

@bp.route('/login', methods = ('GET', 'POST'))
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		error = None
		# ↓Validación de Datos↓
		user = User.query.filter_by(username = username).first()
		if user is None or not check_password_hash(user.password, password):
			error = 'Nombre de usuario o contraseña incorrectos.'

		if error is None:
			session.clear()		#Con ésto vamos a cerrar alguna sesión si esta activa.
			session['user_id'] = user.id	#Vamos a guardar el ID del usuario para no exponer o vulnerar su nombre de usuario.
			return redirect(url_for('todo.index'))

		flash(error)

	return render_template('auth/login.html')

@bp.route('/register', methods = ('GET', 'POST'))
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		user = User(username, generate_password_hash(password))	# Creación del objeto User

		error = None
		user_name = User.query.filter_by(username = username).first()	# Búsqueda en la BD de un nombre de usuario que coincida con el que estamos intentando registrar.

		if user_name is None:	# Si el nombre de usuario no existe, procedemos a registrar al usuario en la BD.
			db.session.add(user)	# Añadir usuario
			db.session.commit()	# Commit de la sesión
			return redirect(url_for('auth.login'))	# Redirección a la página de login.
		else:
			error = f'El usuario {username} ya ha sido registrado previamente.'

		flash(error)

	return render_template('auth/register.html')

#Función para mantener la sesión activa:
@bp.before_app_request	#Antes de cada solicitud se ejecutara lo que haya debajo de éste decorador.
def load_logged_in_user():
    user_id = session.get('user_id')	#A traves del módulo [ session ] es que nosotros vamos a recuperar el ID del usuario y lo vamos a guardar en ésta variable.

    if user_id is None:
        g.user = ''
    else:
        g.user = User.query.get_or_404(user_id)

@bp.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))

#Función para requerir auntenticación para acceder a la To-Do List, porque es sencillo hacerlo a traves de la url, entonces ésta es una pequeña medida de seguridad.
import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
#Notas sobre el módulo g:
# El módulo [ g ] en Flask es un objeto global que se puede utilizar para almacenar datos durante el ciclo de vida de una solicitud. Se usa para almacenar datos que están relacionados con la solicitud actual, pero que no necesariamente deben ser pasados de una función a otra a través de argumentos.
# El objeto [ g ] se almacena en la aplicación Flask y se puede utilizar en todas las funciones que se llaman durante la solicitud actual. Es decir, es una forma de compartir datos entre funciones en una solicitud sin pasar explícitamente los datos como argumentos.
# Por ejemplo, si tienes un sitio web que requiere autenticación, puedes almacenar la información de usuario actual en el objeto [ g ] para que esté disponible en todas las funciones que se llamen durante la solicitud actual. También se puede usar para almacenar una conexión de base de datos, datos de configuración, etc.

#* Nota sobre la función [ login_required ]
#Lo que hace en pocas palabras es primero hacer una pausa antes de permitir el acceso a la vista, pausa ocupada para que se verifique si hay un usuario loggeado y dependiendo de ello saber a donde redireccionar.
# La función login_required es un decorador que se utiliza para proteger una vista en Flask. Esta función toma una vista (función que maneja una solicitud HTTP) como argumento y devuelve una nueva vista (también una función) que protege la vista original.
# En la implementación, la función wrapped_view se crea y se retorna como una nueva vista que encapsula la vista original. La función wrapped_view comprueba si hay un usuario autenticado en g.user. Si no hay usuario, redirige al usuario a la página de inicio de sesión utilizando la función redirect(url_for('auth.login')). Si hay un usuario, se llama a la vista original utilizando la función view(**kwargs) y se devuelve el resultado.
# La función functools.wraps se utiliza para asegurarse de que la nueva vista tenga el mismo nombre y docstring que la vista original. Esto es importante porque ayuda a mantener la coherencia en la documentación de la aplicación.