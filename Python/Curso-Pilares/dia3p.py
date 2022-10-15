"""#Imprime toda la lista:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

#Imprime un valor de la lista:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[1])

#Imprime dos valores de la lista, debe ser por rango:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[0:2])

#Imprime un rango de la lista:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[2:5])

#Imprime un rango de la lista con saltos:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[0:9:2]) #Este tercer valor es el que dicta cada cuantos valores hace un salto

#Imprime los números de atras hacia delante:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[::-1])

#Podemos sumar listas:
lista2 = [10, 11, 12, 13 ,14, 15, 16, 17, 18, 19]
print(lista + lista2)

#Podemos sumar partes de las listas:
print("Este es el ejercicio:")
print(lista[1:4] + lista2 [6:8])

#Podemos multiplicar:
print(lista * 3)

#Para hacer un cambio de valor en una lista:
lista[2] = 44 #En el valor 2 de la lista se se asignara el nuevo valor 44.
print(lista)

#Metodos o funciones de las listas:
    #lista.append()
    #lista.insert()
    #lista.extend()
    #lista.index()
    #lista.remove()
    #lista.pop()
    #lista.count()

#Añade un valor al final:
lista.append(999)
print(lista)

#Indicas la poscision y el valor a añadir:
lista.insert(3, "INSERT")
print(lista)

#Añade una multitud de valores, se debe hacer como lista, con los corchetes []:
lista.extend(["n1", "n2", 9])
print(lista)

#nos devuelve la posición de un valor:
print(lista.index(5)) #EL valor que haya dentro (5), el index os dará el número de su valor.
#Si hay doa valores iguales dará la pocosion del primer valor que encuentre.

#nos ayuda a remover o eliminar un valor:
lista.remove("INSERT") #Tenemos que añadir el valor a eliminar, no su posicion.
print(lista)

#Para emilimar un valor por posición:
lista.pop(10)
print(lista)

#Cuenta los valores dentro de una lista:
print(lista.count(9))"""

"""#Tuplas: Son colecciones de datos que no neceariamente tiene que ser del mismo tipo.
    #Se definen con parentesis.
    #Son listas que unavez definidas no se pueden modificar.
    #Se pueden convertir listas a tuplas y tuplas a listas.
lista = [1, 2, 3, 4, 5]
tupla = (6, 7, 8, 9, 10)
print(type(lista))
print(type(tupla))

#Estamos haciendo que una lista sea una tupla:
#Estamos haciendo que una tupla sea una lista:
lista = tuple(lista)
tupla = list(tupla)
print("Acá ya estam cambiados los tipos de datos")
print(type(lista))
print(type(tupla))
#los metodos que se pueden ocupar con las Tuplas solo son: Index y Count. Puesto que las tuplas son valores inmutables.
frase = ("En Bagdad", "morada de paz", "en los tiempos del califa Harun al Rashid")
print(type(frase))
print(len(frase)) #el prefijo len nos dirá la longitud de una variable:"""

#Diccionarios (dict):
    #Son estructuras de datos que nos permiten almacenar valores de diferente tipo de datos.
    #Un elemento de un diccionario esta asociado a dos valores: llave : valor.
        #Se separan con coma para añadir valores "lave1":"valor1", "llave2":"valor2".
    


"""#Creación de un diccionario: para crear uno se ocupan las llaves {}
diccionario = {'llave':"valor asociado a la llave", 'nombre':"juan", 'apellido':"gonzales", 'profesion':"contador"}

#Metodos de los diccionarios:
    #diccionario.key() Me da el ID de la llave.
    #diccionario.values() Me da los valores.
    #diccionario.items() Me da la asociación llave:valor, o todo.

#Acá estamos suplantando el valor juan por javier de la llave [nombre]:
diccionario['nombre'] = "javier"

#Añadiremos una nueva key con su valor:
diccionario['eSport'] = "Street Fighter"
print("keys:")
print(diccionario.keys())
print("Values:")
print(diccionario.values())
print("Items")
print(diccionario.items())"""

#Practicas:
    #1.-Programa que pida al usuario un número e como resultado imprima si el número es positivo o negativo 
"""
def pos_neg(a):
    if a == 0:
        return print("Tú número es cero")
    elif a > 0:
        return print("Tú número es positivo")
    else:
        return print("Tú número es Negativo")
n = int(input("Favor de ingresar un número: "))
pos_neg(n)
"""
    #2.-Programa que pida al usuario un número e imprima si el número ingresado esta en el rango de 1 a 7 
"""
def siete(a):
    if a >= 1 and a <=7:
        return print("Tú número es valido")
    else:
        return print("Tú número es Invalido")
n = int(input("Favor de ingresar un número: "))
siete(n)
"""
    #3.-Programa que pida una cantidad al usuario, y también un interés mensual.
    # Si el interés mensual es mayor a 30% indicarle al usuario que el interés es incorrecto.
    # En caso contrario mostrar como resultado el interés que el usuario tiene que pagar con las cantidades ingresadas.
"""
def cuenta(a, b):
    if a >= 1 and a <= 30:
        return print(f"El interes a pagar de {a}, al interes {b} es de: {a * b}")
    else:
        return print("El monto es incorrecto")

n = int(input("¿Cuanto dinero deseas ingresar? "))
im = int(input("¿En cuanto interes mensual deseas invertir? "))
cuenta(im, n)
"""