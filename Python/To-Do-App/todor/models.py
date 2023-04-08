from todor import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)        # Creamos los campos que serán usados en la BD, aquí se indica que sera un número y que será también su primary_key.
    username = db.Column(db.String(20), unique=True, nullable=False)    # Aquí inidcamos una cadena de caracteres de hasta 20 de ellos, el dato va a ser único y no puede estar vacío.
    password = db.Column(db.Text, nullable=False)       # Aquí se dice que será texto (pues será formateado por ser contraseña) y tampoco puede estar vacío.

    # Esta clase (el constructor) es para crear los objetos relacionados al usuario.
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # Creamos los campos que serán usados en la BD, aquí se indica que sera un número y que será también su primary_key.
    create_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)     # Vamos a crear una llave foranea para indicar que UN usuario puede tener MUCHAS tareas. Lo que se ve en [('user.id')] es el acceso al objeto de la clase anterior, directamente a su id.
    title = db.Column(db.String(100), nullable=False)   # Aquí indicamos una cadena de caracteres de hasta 100 de ellos, no puede estar vacío.
    desc = db.Column(db.Text)       # Aquí se dice que será texto (pues será formateado por ser contraseña) y tampoco puede estar vacío.
    state = db.Column(db.Boolean, default=False)        # Indicamos que será de tipo booleano y por defecto será falso.

    # Esta clase (el constructor) es para crear los objetos.
    def __init__(self, create_by, title, desc, state = False):
        self.create_by = create_by
        self.title = title
        self.desc = desc
        self.state = state

    # Esta clase es para mostrar/representa el nombre de la tabla en la base de datos.
    def __repr__(self):
        return f'<To-Do: {self.title} >'
