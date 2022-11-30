import sqlite3

class ConexionDB:
    def __init__(self):
        self.baseDDatos = 'database/Libros.db' #Estamos estableciendo una ruta para el archivo.
        self.conexion = sqlite3.connect(self.baseDDatos)    #Establecemos el objeto de la conexción al archivo.
        self.cursor = self.conexion.cursor()    #Éste es el objeto que se encarga de escribir.

    def cerrarDB(self):
        self.conexion.commit()  #Se encarga de guardar los cambios.
        self.conexion.close()   #Se encarga de cerrar el archivo.
    #Se hace ésta función para que guarde y cierre e una misma llamada.