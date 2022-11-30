from .ConexionDB import ConexionDB #Como estamos dentro de model, solo se debe poner el punto y se da por sentado que el archivo viene de éste paquete
from tkinter import messagebox

#Aquí vamos a crear las acciones de los sub-botones del botón [ Inicio ]
def crearTabla():
    conexion = ConexionDB()
#Si puedes crear éste campo directamente desde SQLite, mejor.
    sql = """
    CREATE TABLE "Libros" (
        "id_libro"	INTEGER,
        "titulo" TEXT,
        "autor"	TEXT,
        "editorial"	TEXT,
        "pais"	TEXT,
        "formato" TEXT,
        PRIMARY KEY("id_libro" AUTOINCREMENT)
    )"""
    try:    #Para evitar errores ponemos la sentencia try:
        conexion.cursor.execute(sql)
#El objeto conexión que contiene la clase ConexionDB ejecutará el texto.cursor que pusimos en la variable sql,
    #y como tiene lenguaje de SQL pues va a funcionar como un intermediario.
        conexion.cerrarDB()     #Lllamamos el método que guarda y cierra. 
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)    #Mandamos un mensaje al usuario para que quedé enterado.
    except:
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)

#Abajo vamos a hacer lo mismo pero con comandos para borrar a tabla.
def borrarTabla():
    conexion = ConexionDB()
    sql = 'DROP TABLE Libros'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla en la base de datos se borro con éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No existe esa tabla en la base de datos'
        messagebox.showerror(titulo, mensaje)

#Ahora podemos ir al archivo principal, importar [ from model.librosdb.py import crearTabla, borrarTabla  ]
# y dentro de la función barraMenu, en los commandos de crear y borrar registro metemos estas funciones como command.

class Libro:    #La clase para crear la tabla y registrar los datos de ésta.
    def __init__(self,titulo:str, autor:str, editorial:str, pais:str, formato:str): #, leido:str
        self.id_Libro= None
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.pais = pais 
        self.formato = formato 
        # self.leido = leido
    
    def __str__(self):
        return f'Libro: {self.titulo}, {self.autor}, {self.editorial}, {self.pais}, {self.formato}' #, {self.leido}

def registrarDatos(Libro):  #Estamos pidiendo que se le pase una clase o en éste caso, la misma clase.
    conexion= ConexionDB()

    sql= f'''INSERT INTO Libros (titulo, autor, editorial, pais, formato)
    VALUES ("{Libro.titulo}", "{Libro.autor}", "{Libro.editorial}", "{Libro.pais}", "{Libro.formato}")''' #De arriba quite:, leido | de abajo:, "{Libro.leido}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
    except:
        titulo= 'Conexión al Registro'
        mensaje= 'La tabla "Libros" no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)
#Una vez creada ésta clase nos vamos a gui_app.py, a la función de guardarDatos y ahí creamos un objeto de ésta clase.

#Esta función nos servirá para capturar los datos de la base de datos para después ponerla en la interfaz:
def listar():
    conexion= ConexionDB()
    listaLibros= []
    sql= "SELECT * FROM Libros"
    try:
        conexion.cursor.execute(sql)
        listaLibros= conexion.cursor.fetchall()   #Con ésto la lista recupera la información en la lista, gracias al comando de sql
        conexion.cerrarDB()
    except:
        titulo= 'Conexión al Registro'
        mensaje= 'La tabla Libros no esta creada en la base de datos'
        messagebox.showwarning(titulo, mensaje)
        
    return listaLibros
#Ahora nos vamos al archivo gui_app.py y dentro de la función 'tablaDatos' ponemos esta funci+on arriba de todo.

#Función para editar los registros:
def editarRegistro(Libro, id_Libro):    #(objeto.Libro, id_Libro)
    conexion= ConexionDB()              #Se crea la conexión

    sql= f'''UPDATE Libros
    SET titulo = "{Libro.titulo}", autor = "{Libro.autor}", editorial = "{Libro.editorial}", pais = "{Libro.pais}", formato = "{Libro.formato}"
    WHERE id_libro = "{id_Libro}"'''  #Hacemos el ejecutable de SQL
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
    except:
        titulo= 'Edición de datos'
        mensaje= 'No se ha podido editar éste registro'
        messagebox.showerror(titulo, mensaje)
#Ahora debemos poner ésta función en gui_app.py y crearemos una nueva función para

#Vamos a hacer la función para eliminar un registro:
def eliminarRegistro(id_libro):
    conexion= ConexionDB()
    sql= f'DELETE FROM Libros WHERE id_libro = "{id_libro}"'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
    except:
        titulo= 'Eliminar Datos'
        mensaje= 'No se puede eliminar éste registro'
        messagebox.showerror(titulo, mensaje)
        
#Ahora vamos a gui y creamos un nuevo método para poder usar éste y ponerlo en el boton.
