from io import open
import secrets

#Voy a ampezar declarando un inpur para guardar la palabra y después lo guardaré en otra variable para tener copia.
palabra= input('Ingresa la palabra de la cual quieras anagramas: ').upper()
palabra = list(palabra)
copia= []   #Aquí se guardará una copia de 'palabra'.
lista= []   #Para almacenar y después regresar a su estado normal.
serie= []   #Para guardar los resultados.

#Primero vamos a crear la función para poder meter los anagramas en un archivo de texto:
def crearArchivo(variable):
    archivo= open('anagramas.txt', 'w')
    archivo.writelines(variable)
    archivo.close()

#Ahora una función que tome un elemento de una lista y lo borré para no tener alementos repetidos.
def tomayBorra(x:list):     #Recibe una lista.
    z = secrets.choice(x)   #Var:Z = Método que selecciona un elemento al azar de la lista.
    x.remove(z)             #A la lista ingresada se le borra el elemento seleccionado previamente (para que no se duplique).
    return z                #Regresas Var:Z

for i in palabra:   #Tuve que crear así la copia porque si trataba de hacer una copia directa [copia = palabra], me daba error.
    copia.append(i)
num= len(copia)

digito= int(input('Ingresa cuántas variantes quieres: '))
while digito != 0:              #Mientras que digito no sea cero:
    for i in range(num):   #Cliclo FOR en el rango de la longitud de la primer palabra.
        z = tomayBorra(palabra)         #Var:z = la función descrita arriba.
        lista.append(z)                 #Le añadimos ESA letra conseguida a lista:list
        if len(copia) == len(lista):           #Si la longitud de palabra llega a cero:
            comodin= ''.join(lista)         #guardamos lo que hay en la lista dentro de comodín
            if comodin in serie:            #Si comodín está en la lista serie
                pass
            else:                           #SINO:
                serie.append(comodin)           #Añado comodín a la lista serie que guardará las palabras.
                serie.append(' - ')             #y le añado una separación para que al escribirlo no que queden todos lo elementos pegados.
                lista= []                       #Dejo la lista vacia para que quedé disponible y no meta repetidos.
                for i in copia:                 #Palabra vuelve a tener su valor de antes y regresar a ciclo.
                    palabra.append(i)
                print(digito)
    digito -= 1

crearArchivo(serie)        
print('Finalizó el proceso')