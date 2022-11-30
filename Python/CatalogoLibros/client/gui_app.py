import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model import librosdb as ldb
from model.librosdb import listar, editarRegistro, registrarDatos, eliminarRegistro

def barraMenu(root):
    barraMenu = tk.Menu(root)   #Declaramos la variable 'barraMenu' y le asignamos el método Menu de la libreria tkinter.
    root.config(menu=barraMenu, width=300, height=300)    #Establecemos unas configuraciones como
    
    menuInicio = tk.Menu(barraMenu, tearoff=0)  #Creamos la variable menuInicio que será la primera opción.
    barraMenu.add_cascade(label='Inicio', menu=menuInicio)  #Bautizamos con 'label' y
#Secciones desplegables del menu Inicio:
    menuInicio.add_command(label= 'Crear registro en BD', command= ldb.crearTabla)  #Acá éstan las funciones que hay dentro de librosdb.py
    menuInicio.add_command(label= 'Borrar registro en BD', command= ldb.borrarTabla)
    menuInicio.add_command(label= 'Salir', command= root.destroy)

    # menuConfi = tk.Menu(barraMenu, tearoff=0)  #Creamos la variable menuInicio que será la primera opción.
    # barraMenu.add_cascade(label='Configuración', menu=menuConfi)  #Bautizamos con 'label' y

    menuHelp = tk.Menu(barraMenu, tearoff=0)  #Creamos la variable menuInicio que será la primera opción.
    barraMenu.add_cascade(label='Ayuda', menu=menuHelp)  #Bautizamos con 'label' y


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=700, height=700)
        self.root = root
        self.pack()
        self.config(bg= '#cdb295')
        self.tabla = ttk.Treeview(self, columns= ('Títulos',"Autor",'Editorial',"País",'Formato'))  #Le quité el ,"Leído"
        self.id_Libro= None

        self.camposLibros()
        self.habilitarCampos()
        self.deshabilitarCampos()
        self.tablaDatos()

#Ésta clase nos va a servir para poder ajustar el FRAME o Recuadro que es la ventana principal.
# En la línea 3 estamos Definiendo la clase, haciendola heredera de el método Frame del Método tkinter.
# Nosotros podríamos simplemente escribir dentro dell archivo principal:
    # def main():
    #     root = tk.Tk()  
    #     root.title('Catalógo de Libros')    
    #     root.iconbitmap('img/LibroIcon.ico')
    #     root.resizable(0,0) 
    #     ===========Frame Section=============
    #     frame.tk.Frame(root) ->Declarando la variable frame y añadiendole el método tk.Frame(asignandolo a root)
    #     frame.pac            ->Empaquetando el tamaño de la ventana al contenido
    #     frame.confing(ancho, alto, color, etc)
    #     ===========Frame Section=============
    #     root.mainloop()
# Pero en lugar de eso tenemos una clase para dejar todo más ordenado o limpió.
# Solo resta importar ésta clase al archivo principal y declararlo en una variable que se conevrtirá en un objeto llamado 'app'.

    def camposLibros(self):
        self.labelTitulo = tk.Label(self, text='Título')    #Creación del objeto y asignación de su nombre.
        self.labelTitulo.config(font= ('Verdana', '12', 'bold'),bg='#cdb295')    #Configuración de la fuente.
        self.labelTitulo.grid(column=0, row=0, padx=5, pady=5)      #Configuración de la posición.

        self.labelAutor = tk.Label(self, text='Autor')    #Creación del objeto y asignación de su nombre.
        self.labelAutor.config(font= ('Verdana', '12', 'bold'),bg='#cdb295')    #Configuración de la fuente.
        self.labelAutor.grid(column=0, row=1, padx=5, pady=5)      #Configuración de la posición.

        self.labelEditorial = tk.Label(self, text='Editorial')    #Creación del objeto y asignación de su nombre.
        self.labelEditorial.config(font= ('Verdana', '12', 'bold'),bg='#cdb295')    #Configuración de la fuente.
        self.labelEditorial.grid(column=0, row=2, padx=5, pady=5)      #Configuración de la posición.

        self.labelPais = tk.Label(self, text='País')    #Creación del objeto y asignación de su nombre.
        self.labelPais.config(font= ('Verdana', '12', 'bold'),bg='#cdb295')    #Configuración de la fuente.
        self.labelPais.grid(column=0, row=3, padx=5, pady=5)      #Configuración de la posición.

        self.labelFormato = tk.Label(self, text='Formato')    #Creación del objeto y asignación de su nombre.
        self.labelFormato.config(font= ('Verdana', '12', 'bold'),bg='#cdb295')    #Configuración de la fuente.
        self.labelFormato.grid(column=0, row=4, padx=5, pady=5)      #Configuración de la posición.
    
        # self.labelLeido = tk.Label(self, text='Leído')    #Creación del objeto y asignación de su nombre.
        # self.labelLeido.config(font= ('Verdana', '12', 'bold'),bg='#cdb295')    #Configuración de la fuente.
        # self.labelLeido.grid(column=0, row=5, padx=5, pady=5)      #Configuración de la posición.

    #Acá abajo vamos a poner lo necesario para los campos de llenado, su nombre son entrys:
        self.miTitulo = tk.StringVar()  #El método StringVar nos permite capturar y mandar los datos del entry.
        self.entryTitulo = tk.Entry(self, textvariable= self.miTitulo)   #Se crea el objeto.
        self.entryTitulo.config(width=50,font= ('Verdana', '12'))
        self.entryTitulo.grid(column=1, row=0, padx=5, pady=5,columnspan=2)

        self.miAutor = tk.StringVar()
        self.entryAutor = tk.Entry(self, textvariable= self.miAutor)   #Se crea el objeto.
        self.entryAutor.config(width=50,font= ('Verdana', '12'))
        self.entryAutor.grid(column=1, row=1, padx=5, pady=5,columnspan=2)

        self.miEditorial = tk.StringVar()
        self.entryEditorial = tk.Entry(self, textvariable= self.miEditorial)   #Se crea el objeto.
        self.entryEditorial.config(width=50,font= ('Verdana', '12'))
        self.entryEditorial.grid(column=1, row=2, padx=5, pady=5,columnspan=2)

        self.miPais = tk.StringVar()
        self.entryPais = tk.Entry(self, textvariable= self.miPais)   #Se crea el objeto.
        self.entryPais.config(width=50,font= ('Verdana', '12'))
        self.entryPais.grid(column=1, row=3, padx=5, pady=5,columnspan=2)

        self.miFormato = tk.StringVar()
        self.entryFormato = tk.Entry(self, textvariable= self.miFormato)   #Se crea el objeto.
        self.entryFormato.config(width=50,font= ('Verdana', '12'))
        self.entryFormato.grid(column=1, row=4, padx=5, pady=5,columnspan=2)

        # self.miLeido = tk.StringVar()
        # self.entryLeido= tk.Entry(self, textvariable=self.miLeido)
        # self.entryLeido.config(width=50,font= ('Verdana', '12'))
        # self.entryLeido.grid(column=1, row=5, padx=5, pady=5, columnspan= 2)

    #Ahora a poner los botones debajo de éstos campos:
        self.botonNuevo = tk.Button(self, text='Nuevo', command= self.habilitarCampos)
        self.botonNuevo.config(width=20, font= ('Verdana', '12', 'bold'),
                fg='#ffffff', bg='#1aa478', cursor='hand2', activebackground='#1b9971')
        self.botonNuevo.grid(column=0, row=6, padx=5, pady=5)

        self.botonGuardar = tk.Button(self, text='Guardar', command= self.guardarDatos)
        self.botonGuardar.config(width=20, font= ('Verdana', '12', 'bold'),
                fg='#ffffff', bg='#019faf', cursor='hand2', activebackground='#0f929f')
        self.botonGuardar.grid(column=1, row=6, padx=5, pady=5)
        
        self.botonCancelar = tk.Button(self, text='Cancelar', command= self.deshabilitarCampos)
        self.botonCancelar.config(width=20, font= ('Verdana', '12', 'bold'),
                fg='#ffffff', bg='#cc3535', cursor='hand2', activebackground='#b93a3a')
        self.botonCancelar.grid(column=2, row=6, padx=5, pady=5)

    # def clicked(self):
    #     print(self.biFavorito.get(), self.biLeido.get())

    def habilitarCampos(self):
        self.entryTitulo.config(state='normal')
        self.entryAutor.config(state='normal')
        self.entryEditorial.config(state='normal')
        self.entryPais.config(state='normal')
        self.entryFormato.config(state='normal')
        # self.entryLeido.config(state='normal')
    #Arriba, los entrys, abajo, los botones.
        self.botonGuardar.config(state='normal')
        self.botonCancelar.config(state='normal')
    #Envió de datos vacios.
        self.miTitulo.set('')
        self.miAutor.set('')
        self.miEditorial.set('')
        self.miPais.set('')
        self.miFormato.set('')
        # self.miLeido.set('')

    def deshabilitarCampos(self):
        self.id_Libro= None
        self.entryTitulo.config(state='disabled')
        self.entryAutor.config(state='disabled')
        self.entryEditorial.config(state='disabled')
        self.entryPais.config(state='disabled')
        self.entryFormato.config(state='disabled')
        # self.entryLeido.config(state='disabled')
    #Arriba, los entrys, abajo, los botones.
        self.botonGuardar.config(state='disabled')
        self.botonCancelar.config(state='disabled')
    #Envió de datos vacios.
        self.miTitulo.set('')
        self.miAutor.set('')
        self.miEditorial.set('')
        self.miPais.set('')
        self.miFormato.set('')
        # self.miLeido.set('')

    def guardarDatos(self):
        libro = ldb.Libro(  #Éste objeto que creamos contendrá todos los valores de los entrys...
        self.miTitulo.get(),
        self.miAutor.get(),
        self.miEditorial.get(),
        self.miPais.get(),
        self.miFormato.get(),
        # self.miLeido.get(),
        )
        #Condicional del boton para guarar o actualizar.
        if self.id_Libro == None:
            registrarDatos(libro)   #...Y después los guardaremos en la tabla con el método que creamos previamente.
        else:
            editarRegistro(libro, self.id_Libro)

        self.tablaDatos() 
        self.deshabilitarCampos()
        
    def tablaDatos(self):
        self.listaLibros = listar() #Estamos añadiendo la lista con los datos.
        self.listaLibros.reverse()  #Ponemos el método .reverse() para que nos aparezca en orden descendente.

        self.tabla = ttk.Treeview(self, columns= ('Títulos',"Autor",'Editorial',"País",'Formato'))  #Le quité el ,"Leído"
        self.tabla.grid(column=0, row=7, columnspan=4,padx=5,pady=5,sticky='nse')    #Busca añadir un rowspan para la tabla.
    #Arriba es la creación de la tabla y su formato, abajo el objeto de la scrollbar:
        self.yscroll= ttk.Scrollbar(self, orient='vertical', command= self.tabla.yview)
        self.yscroll.grid(row=7, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand= self.yscroll.set)
    #Intento de poner scrollbar horizontal
    #abajo los encabezados de las tablas:
        self.tabla.heading('#0', text='ID') #El primer valor es la posición en la columna y el segundo el texto.
        self.tabla.heading('#1', text='Título')
        self.tabla.heading('#2', text='Autor')
        self.tabla.heading('#3', text='Editorial')
        self.tabla.heading('#4', text='País')
        self.tabla.heading('#5', text='Formato')
        # self.tabla.heading('#6', text='Leído')
    ##Después en el apartado donde hicimos una inserción manual vamos a poner in ciclo for para iterar la lista recien importada:
        for dato in self.listaLibros:
            self.tabla.insert('',0, text=dato[0], values=(dato[1], dato[2],dato[3],dato[4],dato[5]))
    #Arriba estamos diciendole que los datos capturados de la base de datos, los ponga en la tabla de nuestra interfaz.
    #Abajo los botones de [ Editar | Eliminar ]
        self.botonEditar = tk.Button(self, text='Editar', command= self.editarDatos)
        self.botonEditar.config(width=10, font= ('Verdana', '12', 'bold'),
                fg='#ffffff', bg='#1aa478', cursor='hand2', activebackground='#1b9971')
        self.botonEditar.grid(column=0, row=8, padx=5, pady=5)
        
        self.botonEliminar = tk.Button(self, text='Eliminar', command= self.eliminarDato)
        self.botonEliminar.config(width=10, font= ('Verdana', '12', 'bold'),
                fg='#ffffff', bg='#cc3535', cursor='hand2', activebackground='#b93a3a')
        self.botonEliminar.grid(column=1, row=8, padx=5, pady=5)    #Si le añades un rowspan a la tabla ajusta éste.

    def editarDatos(self):
        try:
            self.id_Libro= self.tabla.item(self.tabla.selection())['text']
            self.tituloLibro= self.tabla.item(self.tabla.selection())['values'][0]
            self.autorLibro= self.tabla.item(self.tabla.selection())['values'][1]
            self.editorialLibro= self.tabla.item(self.tabla.selection())['values'][2]
            self.paisLibro= self.tabla.item(self.tabla.selection())['values'][3]
            self.formatoLibro= self.tabla.item(self.tabla.selection())['values'][4]
        #Arriba estamos recuperando los datos, abajo vamos a habilitar los campos y debajo llenar los entrys:
            self.habilitarCampos()
            self.entryTitulo.insert(0, self.tituloLibro)
            self.entryAutor.insert(1, self.autorLibro)
            self.entryEditorial.insert(2, self.editorialLibro)
            self.entryPais.insert(3, self.paisLibro)
            self.entryFormato.insert(4, self.formatoLibro)
        except:
            titulo='Conexión al Registro'
            mensaje= 'No es posible Actualizar el registro'
            messagebox.showerror(titulo, mensaje)
#Ahora llevaremos ésta función al boton de editar en su respectivo command, pero...
#...si mandamos los datos en los entrys y guardamos, lo que pasará será que crearemos
# un nuevo registro en lugar de editar el que queremos, por ello pondremos una condicional en el botón guardar:
#Para ello debemos poner primero el atributo [ self.idLibro= None ] en el constructor para poder usar la condicional.

    def eliminarDato(self):
        try:
            self.id_Libro= self.tabla.item(self.tabla.selection())['text']
            eliminarRegistro(self.id_Libro)
            self.tablaDatos()
            self.id_Libro= None
        except:
            titulo='Eliminar un Registro'
            mensaje= 'No se ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)
