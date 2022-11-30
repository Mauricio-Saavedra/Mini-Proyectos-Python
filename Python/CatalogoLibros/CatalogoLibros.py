import tkinter as tk
from client.gui_app import Frame, barraMenu

def main():
    root = tk.Tk()  #START: Crea la ventana o interfaz grafica, se le llama root por ser la raíz.
    root.title('Catálogo de Libros')    #Como su nombre lo índica es para ponerle el titulo a la ventana
    root.iconbitmap('img/LibroIcon.ico')#Para poner un icono personalizado a la raíz.
    root.resizable(False,False) #Da la opción de poder un tamaño fijo a la ventana, o de bloquear el ensanchamiento de algun lado (eje xy), solo acepta valores 0-1, equivalentes a False-True
    barraMenu(root)

    app = Frame(root)   #Éste es el objeto que contiene todo lo que está dentro de la ventana.
    app.mainloop() #ENDO: Es el "Cierre de Flujo", indica cuándo finaliza. El programa acaba al cerrar la ventana.

if __name__ == '__main__':
    main()
# Sé que todo se ejecuta desde éste archivo, lo que no sé aún es si ésto es lo que se empaqueta para sacar el
# acceso directo a la aplicación, vaya, un ejecutable.