# Decisión simple: "if":
# n = 10
# if n > 0: #los dos números son para indicar que el bloque e códifo siguiente es parte de la línea anterior
#      print("tú número es positivo")
# else:
#     pass #Este pass es para que la sentencia else exista pero sea ignorada con el pass, literal la sentencia dice safo

# Decisión doble es solo if o else, pero tamién podemos anidar un if dentro de otro, en este caso este código se lee así:
#     Si "nu" es diferente a 0 ingresamos a la siguiente condicional, sino (else) imprimer Es cero
#         Segúnda condicional:
#         Una vez que vimos que el número es diferente a cero:
#             Si el número es menor que cero es negativo,
#             Si el número es mayor a cero es positivo.
# nu = int(input("Ingresa un número: "))
# if nu != 0:
#     if nu > 0:
#         print("Es positivo")
#     else:
#         print("Es negativo")
# else:
#     print("Es cero")

# Ejercicio de lo ya visto pero que el programa defina si el número es par o impar, lo que hago es hacer una operación con modulo para saber pares o impares:
# nu = float(input("Ingresa un número: "))
# if nu != 0:
#     if nu % 2:
#         print("Es impar")
#     else:
#         print("Es par")
# else:
#     print("Es cero")

# Sentencia elif:
# ¿El número ingresado es mayor a cero?
# Si lo es imprime "Es posotivo"
# Si no entonces "El número cero no tiene signo"
# Si no "es negativo"
# num = int(input("Ingresa un número: "))
# if num > 0:
#     print("Es positivo")
# elif num == 0: #Siempre va antes de un else y después de un if.
#     print("El número cero no tiene signo")
# else:
#     print("Es negativo")

# Ejercicio autoimpuesto de calculadora:
# from ipaddress import summarize_address_range


# n1 = int(input("""Bienvenido a mi primer calculadora
# Por favor ingresa el primer valor: """))
# n2 = int(input("Favor de ingresar el segúndo valor: "))
# s = n1 + n2
# r = n1 - n2
# d = n1 / n2
# m = n1 * n2
# p = n1 ** n2
# m = n1 % n2
# operacion = int(input("""Opciones:
# 1 para sumar
# 2 para restar
# 3 para dividir
# 4 para multiplicar
# 5 para potencia
# 6 para modulo
# Ingresa tu opción: """))
# if operacion == 1:
#     print(s)
# elif operacion == 2:
#     print(r)
# elif operacion == 3:
#     print(d)
# elif operacion == 4:
#     print(m)
# elif operacion == 5:
#     print(p)
# elif operacion == 6:
#     print(m)
# else:
#     print("Valor no valido, intenta de nuevo")

# Aprendiendo funciones para no repetirnos:
# Una función es una "Keyword" que usa parentesis, ejemplo: input()
# -Son un conjunto/bloque de código-instrucciones que realizan una determinada tarea.
# -hay tres mas en tu telefono
# Sintaxis de las funciones:
# def nombre_función(parametro1, parametro2, etc):
#   -instrucciones-código
#   return [opcionar] ||Return también es una Keyword.
# Las variables dentro de la función solo existend dentro, son locales.

"""def suma(): #Esta es una función que cuando seá llamada sumara 2+2
    return 2 + 2 
print(suma())

def suma(a, b): #Esta función sumara a+b, y esos valores serán ingresados a la hora de utilizarse
    return a + b
print(suma(3, 3))

def saludo(username): #Esta función llamada saludo, esta función se dedica a imprimir "hola + el parametro username"
    print("Hola " + username)
name = input("¿Cómo te llamas? ")
saludo(name)"""

# Vamos a definir una función que reciba una calificación del usuario, si es mayor de 10 es invalido, si es mejor a 6 reprobado, si es mayor aprobado.

def calificacion(a): #"a" es una variable generica  que tomara el valor que nosotros le pasemos.
    if a > 10:
        return print("Número invalido")
    elif a < 6:
        return print("Reprobaste")
    else:
        return print("Aprobaste")
nota = int(input("¿cual es tu calificación? "))
calificacion(nota)
# Lo que esta pasando aquí es:
#def: tenemos una función llamada "Calificación" con una posible variable llamada "a" que solo servira dentro de dicha función.
    #if: si "a" es mayor que que 10, daremos un return con print diciendo "Número invalido"
    #elif: si "a" es menor a 6, daremos un return con print diciendo "Reprobaste"
    #else: pero si "a no cumple con ninguna de esas dos condiciones previas", daremos un return con print diciendo "Aprobaste"
    #¿Cómo es esto? Sencillo:
        #Se pone una condicional de SI y NO (IF y ELSE en este caso), si no se cumple if, nos vamos a else.
        #Pero si le añadimos un ELIF (no tiene traducción, pero es una sentencia intermedia) el programa revisa el IF, después los ELIF que haya enmedio, y al final el ELSE.
        # Por eso no es necesario definir el ELSE, porque toma todo aquello que no este dentro de la sentencia.
        