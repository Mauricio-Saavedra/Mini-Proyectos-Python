from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename  # Si la imagen tiene espacios en el nombre, esta función cambia los espacios por guiones bajos.
from .models import User
from BlogMS import db
import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(username, email, generate_password_hash(password)) 

        # Validación de datos:
        error = None
        user_email = User.query.filter_by(email=email).first()  # Obtenemos el email de usuario
        if user_email is None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El correo {email} ya está registrado.'
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validación de datos:
        error = None
        user = User.query.filter_by(email=email).first()  # Obtenemos el usuario

        if user is None or not check_password_hash(user.password, password):
            error = 'Correo o contraseña incorrecto'
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('post.posts'))
        flash(error)
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

def get_photo(id):
    user = User.query.get_or_404(id)
    photo = None
    if photo != None:
        photo = user.photo
    return photo

@bp.route('/profile/<int:id>', methods=('GET', 'POST'))
@login_required
def profile(id):
    user = User.query.get_or_404(id)    #Creamos el objeto del usuario para poder leerlo en la DB y poder modificarlo.
    photo = request.files.get('photo')  # Esto va en las variables de la función, también hay que añadir el photo=photo hasta abajo

    if request.method == 'POST':        #Si el metodo es POST se capturaran los siguientes datos para ser editados.
        user.username = request.form.get('username')
        password = request.form.get('password')

        error = None        #Creamos este None para poder hacer la validación de la contraseña.
        if len(password) != 0:
            user.password = generate_password_hash(password)
        elif len(password) > 0 and len(password) < 8:
            error = 'La contraseña debe tener más de 7 caracteres'

        if photo is not None:
        # if request.files['photo']:  # Si hay una foto en la solicitud del HTML, la guardamos.
            photo = request.files['photo']
            photo.save(f'BlogMS/static/media/{secure_filename(photo.filename)}')  # Sencillo, a secure_filename le estamos enviando el archivo para que se guarde con ese filtro.
            user.photo = f'media/{secure_filename(photo.filename)}'  # En la BD se guardará solamente un string, el nombre del archivo.

        if error is not None:
            flash(error)
        else:
            db.session.commit()
            return redirect(url_for('auth.profile', id = user.id))
        flash(error)
    return render_template('auth/profile.html', user=user, photo=photo)
