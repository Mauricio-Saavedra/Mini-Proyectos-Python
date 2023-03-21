from io import open
import secrets

#Empiezo declarando las variables para almacenar la palabra y una para medir su longitud.
palabra = input('Ingresa la palabra de la cual quieras anagramas: ').upper()
long = len(palabra)

#Sacó el factorial de la longitud de la palabra para decirle al usuario las posibilidades que su palabra tiene.
def factorial(long):
    global num2     #Hago Global la variable que guardará el factorial para usarla después y así evitar una ruptura del código.
    num1 = long
    num1 += 1
    num2 = 1
    for i in range(1, num1):
        num2 *= i 
    print(f'La palabra {palabra} tiene: {num2} combinaciones posibles.')

#Llamo a la función para que se ejecute.
factorial(long)

#Tranformo la palabra en una lista para poder manipularla y una copia para poder resetear la palabra al final de la iteración que la descompone.
palabra = list(palabra)
copia = list(palabra)
serie = []  #Esta guarda todas los anagramas que se vayan haciendo, así como un guion para separarlos.

#Creo una función para crear un archivo de texto en el cual guardar el final todos anagramas.
def crearArchivo(variable):
    with open('anagramas.txt', 'w') as archivo:  # Usamos 'with' para abrir el archivo y evitar tener que cerrarlo después.
        archivo.writelines(variable)

#Creo una función para que de la palabra (ahora lista) se tome una letra y se borre después de tomarla, para así evitar duplicados.
def tomayBorra(x):
    z = secrets.choice(x)
    x.remove(z)
    return z

# Pongo un ciclo infinito que se romperá cuando el usuario introduzca un valor válido.
while True:  
    try:
        digito = int(input('Ingresa cuántas variantes quieres: '))
        if digito < 1:  # Confirmo que el valor ingresado sea válido.
            raise ValueError
        elif digito > num2: # Y también que no sobrepase las posibilidades de su propio factorial.
            raise NameError
        break
    except ValueError:
        print('Ingresa un número entero positivo mayor a cero.')
    except NameError:
        print('Ingresa un número menor o igual a las posibilidades de tu palabra.')

# Uso '_' como una convención para indicar que no usaremos la variable en el ciclo, pero se hace las veces indicadas por el usuario.
for _ in range(digito):  
    lista = []
    for i in range(len(palabra)):   #Un ciclo for con la longitud de la palabra
        z = tomayBorra(palabra)         #Usamos la función que descompondrá la palabra.
        lista.append(z)                 #Vamos ingrasando las letras en la lista vacía.
        if len(copia) == len(lista):    #Si la longitud de la COPIA es igual a la longitud de la lista:
            comodin = ''.join(lista)        #entonces añadimos lo que hay en la lista a la variable COMODIN
            if comodin in serie:            #Si COMODIN esta en SERIE...   
                pass                            #...lo desechamos.
            else:                           #Si no lo está:
                serie.append(comodin)           #A serie le añadimos COMODIN
                serie.append(' - ')             #Le añadimos dos espacios y un guión.
                lista = []                      #Vaciamos de nuevo la lista.
                palabra = list(copia)           #Reiniciamos 'palabra' a su valor original con ayuda de la copia.
    palabra = list(copia)  # Reiniciamos 'palabra' al inicio de cada iteración.

crearArchivo(serie)     #Por último creamos el archivo con todo el contenido de SERIE.
print('Finalizó el proceso.')
