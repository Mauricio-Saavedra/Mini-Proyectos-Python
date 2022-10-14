#Funciones: lambda, map,
#Necesitamos que los valores de una lista del 1 al 10  se guarden en otra lista pero al cubo.
"""
lista = [1,2,3,4,5,6,7,8,9,10]
lista3 = []

#A mi se me ocurrió hacerla co un ciclo FOR:
for i in lista:
    x =  i**3
    lista3.append(x)
print(lista3)

#También se puede dentro de la misma lista:
lista3 = [i**3 for i in lista]
print(lista3)

#O haceerlo con una función:
def cubo(x):
    return x**3
lista3 = [list(map(cubo, lista))]
print(lista3)

#lambda es una función desechable, como lo vemos se define de manera sencilla:
var = lambda x: x**3
print(var(9))

#Pero fucionarlo con map es lo importamte, pues map puede iterar un FUNCION (normal o lambda) con un iterable:
lista3 = [list(map(lambda x: x**3, lista))]
print(lista3)
"""
#Ejercicio1: De una lista con valores string crea una función que guarde en una lista si la primera letra de la palabra es 'a':
#Yo quería que la función en sí misma ya fuese capaz de recorrer toda una lista, pero esto no es necesario,
#pues con hacer que lo haga con una palabra basta, pues con el [ map ] ya podemos hacer que recorra una lista.
""" 
frutas = ['aguacate', 'apple', 'melon', 'sandia', 'apericot']
def inicioA(letra):
    return letra[0] == 'a'
#Así sería con la funcion:
empieza_a = [list(map(inicioA, frutas))]
print(empieza_a)

#Así sería con lambda:
empieza_a = [list(map(lambda x: x[0] == 'a', frutas))]
print(empieza_a)
"""

#FILTER()
#Guarda en unalista los valores que empiecen con la leta 'a':
#Así se haría sin filter:
"""
def inicioA(letra):
    return letra[0] == 'a'


frutas = ['aguacate', 'apple', 'melon', 'sandia', 'apericot']
frutasA = []

for i in frutas:
    fruta = inicioA(i)
    if fruta == True:
        frutasA.append(i)

print(frutasA)

#Así sería con filter:

frutasA2 = list(filter(inicioA, frutas))
print(frutasA2)

#Así sería con filter y lambda:

frutasA3 = list(filter(lambda x: x[0] == 'a', frutas))
print(frutasA3)
"""
#Ejercicio2: filtra de una lista los valores que sean multiplos de 3:
"""
from functools import reduce

lista = [1, 3, 4, 4, 7, 4, 18, 9, 4, 6, 8, 9, 27, 90, 30]
listaf = list(filter(lambda x: x % 3 == 0, lista))
print(listaf)

#REDUCE() ->Es importado<- Ahora sumaré los números:
suma = reduce(lambda x, y: x + y, lista)
print(suma)
"""

#Entornos virtuales:
#Esta es un aherramienta para
#Un modulo es cualquier archivo que tenga código python, estos los podemos importar para usarlos nosotros.
#Un entorno virtual nos va a encapsular un proyecto, para prevenir cambios inesperados de algún modulo y que siempre
#se ejecute de la manera como fue programado.