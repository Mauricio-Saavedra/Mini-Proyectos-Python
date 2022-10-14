# PRACTICA 9 | Alexis Mauricio Saavedra Bueno | Folio: 914NL003.

# 9.1 Ejercicio 1 (2 puntos)
# Realice un programa que pregunte aleatoriamente una multiplicación:
# 1.- El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea
    # incorrecta el programa debe indicar cuál es la correcta).
# 2.- El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos.
"""
import random
x, z = 0, 0
lap, con = 10, 0
def ruleta(x):
    x = random.randrange(2, 52)
    return x
print('Bienvenido al reto matematico, por favor responde las siguientes preguntas:')
while lap != 0:
    xx, zz = ruleta(x), ruleta(z)
    yy = zz*xx
    pregunta = int(input(f'¿Cual es el resultado de {xx} X {zz}? -> '))
    if pregunta == yy:
        lap -= 1
        con += 1
        print('¡Acertaste!')
    else:
        lap -= 1
        print(f'Fallaste, la respuesta correcta era: {yy}.')
print(f'¡Gracias por jugar! tú resultado fue: {con}/10')
"""
# 9.2 Ejercicio 2 (2 puntos)
# Obtener el cuadrado de todos los elementos en la lista.
# Lista: [1,2,3,4,5,6,7,8,9,10]
"""
Lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = list(map(lambda x: x*x, Lista))
print(lista2)
"""
# 9.3 Ejercicio 3 (2 puntos)
# Obtener la cantidad de elementos mayores a 5 en la tupla.
# tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
"""
tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
lista3 = list(filter(lambda x: x > 5, tupla))
print(lista3)
"""
# 9.4 Ejercicio 4 (2 puntos)
# Obtener la suma de todos los elementos en la lista
# lista = [11,22,33,44,55]
"""
from functools import reduce

lista = [11,22,33,44,55]
suma = reduce(lambda x, y: x + y, lista)
print(suma)
print(sum(lista))
"""