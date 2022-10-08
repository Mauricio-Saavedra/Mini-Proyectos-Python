import random
# 1.-Realizar un programa que primero inicialice una lista con 10 valores aleatorios (del 1 al 10)
    # y posteriormente muestre en pantalla cada elemento de la lista junto con sus
    # potencias al cuadrado y al cubo.
"""
lista = []
for i in range(10):     #Declaro el ciclo FOR con un rango 10.
    x = int(random.randrange(1, 50)) #hago una variable "x" para que contenga un número aleatorio.enUnRango(del 1 al 50)
    if x < 51:
        lista.append(x)
print(lista)
for f in lista:
    print(f"{f} Al cuadrado: {f**2} y al cubo: {f**3}")
    # print(f"{x} Al cuadrado es: {x**2} y al cubo es: {x**3}")
"""
# 2.-Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado.
    # Copia los elementos de la lista en otra lista pero en orden inverso,
    # y muestra sus elementos por la pantalla.
"""
lista = []
for i in range(5):
    almacen = input('Ingresa una palabra: ')
    if i < 6:
        lista.append(almacen)
print(lista)
print(lista[::-1])
"""
# 3.-Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
    # (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,
    # la nota media, la nota más alta que ha sacado y la menor.
"""
lista = []
contador = 0
acumulador = 0
while contador < 5:
    nota = int(input('Ingresa tú calificación: '))
    if nota >= 0 and nota <= 10:
        lista.append(nota)
        contador += 1
    else:
        print('Calificación invalida, intenta de nuevo.')
print(f'Tus calificaciones son: \n  {lista}')

for i in lista:
    acumulador += i
print(f'La media de tus calificaciones fue: {acumulador // 5}')

for n in lista:
    mayor = max(lista)
    menor = min(lista)
print(f'Tu mayor nota fue: {mayor},\nTú menor nota fue: {menor}')
"""
# 4.-Codifica un programa en python que nos permita guardar:
    #-> los nombres de los alumnos de una clase y las notas que han obtenido.
    #-> Cada alumno puede tener distinta cantidad de notas.
    #-> Guarda la información en un diccionario cuya claves serán los {nombres} de los
    # alumnos y los valores serán listados con las {notas} de cada alumno.
    #-> El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas
    # hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de
    # alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de
    # un alumno que ya existe el programa nos dará un error.
#Primero declaro dos variables, el diccionario con una primer llave y valor de tipo lista, y un númerador:
alumnos = {}
num = int(input('Ingresa la Cantidad de alumnos: '))
while 0 != num:         #Mientrntas el númerador sea diferente de 0 estaras en ciclo:
    alumno = input('Ingresa el nombre del alumno: ')    #Pido que ingresé el nombre de los alumnos.
    alumnos[alumno] = []    #al diccionario alumnos le agrego el nombre del alumno con Una lista vacía.
    num -= 1        #Le quito uno al númerador para que se acerqué a cero.

for nombre in alumnos.keys():      #Declaro un ciclo FOR en la cantidad de alumnos con la función .keys() para que recorrá las llaves:
    cal = int(input(f'Cuántas calificaciones de {nombre} añadirás: '))   #La variable CAL es aquella que informará cuantas calificaciones tiene que meterse en la lista.
    while 0 != cal:         #Mientras que CAL sea diferente de o estarás en ciclo:
        notas = int(input(f'Introduce la calificación de {nombre}: '))  #Pido las calificaciones del alumno en turno:
        if notas >= 0 and notas <= 10:      #SI notas esta en el raango entre 0 y 10...
            alumnos[nombre] += [notas]     #Entonces al diccionario ALUMNOS en la llave que tanga en ese momento la variable nombre se le agregara el dato de NOTA en la lista más el valor que ya contenga la lista en si misma, esto lo hice así porque no logré conectar el .append().
            cal -= 1        #Restamos uno al contador de calificaciones.
        elif notas <= -1:   #Si la nota es igual o menor a -1, entonces...
            cal = 0         #CAL es igual a cero para pasar a la siguiente llave en el ciclo FOR.
        else:               #SI el número NO est en el rango, entonces mandamos a imprimir un aviso y lanzamos de nuevo el mensaje.
            print('Calificación erronea, intenta de nuevo.')
            notas = int(input(f'Introduce la calificación de {nombre}: '))
#Para finalizar imprimimos el diccioario ALUMNOS.
print(f'----Los alumnos con sus calificaciones:----\n{alumnos}')
#La cuestión es que también debo sacar la media o promedio de las calificaciones.
#Para ello decalro tres variables:
    # Contenedor para guardar la suma de las notas.
    # div para guardar el resultado final.
    # count para contar los números o vueltas que hay dentro de ciclo.
contenedor = 0
div, count = 0, 0
for listas in alumnos.values(): #Hago este ciclo FOR para que la variable LISTAS recorra los valores del diccionario ALUMNOS:
    for i in listas:        #Este ciclo es para que "i" recorrá la lista en sí, o el valor del diccionario:
        count += 1          #Count + 1 a cada vuelta.
        ii = int(i)         #"ii" guardará el item que contenga "i" en dicha vuelta y lo hará un entero.
        contenedor += ii    #Contenedor va sumando los valores de "ii"
        div = contenedor / count    #Acá es cuando se hace la división del total de la suma entre la cantidad de números que hay.
        # print(type(ii), ii, i, contenedor, div)
#me hace falta meter estos valores contenidos en DIV dentro del item del diccionario, buscó reemplazarlos.
    listas.clear()
    listas.append(div)
print(f'Aquí tienes el promedio de los alumnos: {alumnos}')

# 5.-Crea una tupla con los meses del año, pide números al usuario,
    # si el número está entre 1 y la longitud máxima de la tupla,
    # muestra el contenido de esa posición sino muestra un mensaje de error.
    # El programa termina cuando el usuario introduce un cero.
"""
import sys
tupla = ('Cerrar Programa','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
num = int(input('Ingresa un número del 1 al 12: '))
con = 0
while con != 1:
    if num >= 0 and num <= 12:
        if num == 0:
            print('Cerrando programa...')
            sys.exit()
        elif num == 1:
            print(tupla[1])
            con += 1
        elif num == 2:
            print(tupla[2])
            con += 1
        elif num == 3:
            print(tupla[3])
            con += 1
        elif num == 4:
            print(tupla[4])
            con += 1
        elif num == 5:
            print(tupla[5])
            con += 1
        elif num == 6:
            print(tupla[6])
            con += 1
        elif num == 7:
            print(tupla[7])
            con += 1
        elif num == 8:
            print(tupla[8])
            con += 1
        elif num == 9:
            print(tupla[9])
            con += 1
        elif num == 10:
            print(tupla[10])
            con += 1
        elif num == 11:
            print(tupla[11])
            con += 1
        elif num == 12:
            print(tupla[12])
            con += 1
    else:
        print('Número invalido.')
        num = int(input('Ingresa un número del 1 al 12: '))
"""