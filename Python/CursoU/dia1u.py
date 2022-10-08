from cmath import pi
from sqlite3 import TimestampFromTicks
from ssl import OP_NO_TLSv1_1
#LOS BÁSICOS:

# Imprimiendo estos datos empezamos el curso.
# Para volver a acceder a cualquiera de estas lineas de código solo descomentalas.
# print("Hola Power Shell")
# nombre = "Alexis"
# edad = "27 años"
# print(f"Mi nombre es {nombre} y tengo {edad}")

# Acá vamos a sumar dos valores dados por el usuario:
# n1 = int(input("Ingresa tu Primer valor "))
# n2 = int(input("Ingresa tu Segundo valor "))
# print(n1 + n2)

# Ahora vamos a Dividir y obtener el Modulo de dos números dados por el usuario:
# n1 = int(input("Ingresa tu Primer valor "))
# n2 = int(input("Ingresa tu Segundo valor "))
# dividir = n1 / n2
# modulo = n1 % n2
# proceso = int(input("Selecciona 1 para dividir o 2 para sacar el Modulo?"))
# if proceso == 1:
#     print(dividir)
# if proceso == 2:
#     print(modulo)

# # Calcula el precio de venta:
# vv = float(input("Ingresa el valor de venta del producto: "))
# ex = 0.18
# igv = vv * ex
# pv = vv + igv
# print(f"El precio de venta es {pv}, y el IGV es de {igv}")

# Imprimir número de 5 digitos al revez
# n = int(input('Número: '))

# # Solución 
# residuo = n % 10
# n = n // 10
# numeroInverso = residuo * 10

# residuo = n % 10
# n = n // 10 
# numeroInverso = (numeroInverso + residuo) * 10

# residuo = n % 10
# n = n // 10 
# numeroInverso = (numeroInverso + residuo) * 10

# residuo = n % 10
# n = n // 10
# numeroInverso = (numeroInverso + residuo) * 10

# numeroInverso = numeroInverso + n

# # Salida de datos
# print(f'Tú número al revez es:{numeroInverso}')

#Ejercicio de sumar números:
# n = int(input("Ingresa tú número: "))
# s = (n * (n + 1)) / 2
# print(s)

#Visualización de interés:

# capital = float(input("¿Cuánto desea ingresar a su cuenta? "))
# t_interes = 1.04
# tiempo = float(input("¿Por cuantos meses desea invertir? "))
# monto = ((1 + t_interes / 100) ** tiempo) * capital
# interes = monto - capital
# print(f"Su ganancia es {monto}, el interes fue de {interes}")

#Encontrar el área de un circulo, Area = pi * r2

# r = float(input("Cuál es el rario de tu circulo? "))
# pi = 3.14159
# a = pi * r ** 2
# print(a)

# Programa que convierta los segundos en hh:mm:ss

# t = int(input("Favor de ingresar la cantidad que quieres convertir: "))
# h = t / 3600
# m = t / 60
# s = t
# print(f"""Las horas son {h}
# Los minutos son {m}
# Tus segundos son {s}""")