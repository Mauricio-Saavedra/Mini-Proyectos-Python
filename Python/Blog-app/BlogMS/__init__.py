from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
import locale

db = SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config.from_object(config.Config)   #Primer argumento es el archivo y el segundo la clase.
    db.init_app(app)
    ckeditor = CKEditor(app)
    locale.setlocale(locale.LC_ALL, 'es_ES')

    #Registro de vistas:
    from BlogMS import home
    app.register_blueprint(home.bp)

    from BlogMS import auth
    app.register_blueprint(auth.bp)

    from BlogMS import post
    app.register_blueprint(post.bp)

    #Importamos las clases que contienen los modelos de los usuarios y los post, así como los creamos.
    from .models import User, Post 
    with app.app_context():
        db.create_all()

    return app