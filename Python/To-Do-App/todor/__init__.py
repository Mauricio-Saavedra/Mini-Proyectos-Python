from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():       #Esta vez hacemos la declaración de la app dentro de una función, pues es más escalable y modular, ya que permite separar la configuración de la aplicación y las rutas en diferentes módulos y paquetes. Además, este enfoque facilita la reutilización del código de la aplicación en diferentes contextos, como pruebas unitarias o despliegues en diferentes entornos.
    app = Flask(__name__)
    # ↓Configuraciones del proyecto↓
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'houdinni',
        SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"
    )
    # ↑Configuraciones del proyecto↑
    
    # ↓Inicializamos la base de datos↓
    db.init_app(app)
    
    # ↓Registro de BluePrints↓
    from . import todo
    app.register_blueprint(todo.bp)
        # ↓Registro de la BD↓
    from . import auth
    app.register_blueprint(auth.bp)
    # ↑Registro de BluePrints↑
    #, name='auth_v2'

    @app.route('/')
    def index():
        return render_template('index.html')
    
    # ↓Creamos las tablas en la base de datos↓
    with app.app_context():
        db.create_all()

    return app