#CONDICIONALES IF--ELIF--ELSE:
#Crear un sistema que detecte si número es par positivos o par negativo y también si es impar positivo o negativos y si el numero ingresado es 0 que detecte si es neutro.
"""def juez(a):
    if a == 0:
        return print("Tú número es cero.")
    elif a < 0:
        return print("Tú número es negativo.")
    else:
        return print("Tú número es positivo.")

acuzado = int(input("Favor de ingresar un valor: "))
juez(acuzado)"""
#Me salió increible 10/10
"""
#Crear un sistema que detecte si un carácter es vocal o no
def maestro(l):
    if l == int:
        return print("Tu caracter es un número, favor de ingresar una letra")
    elif l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        return print("Tu caracter es una vocal")
    else:
        return print("Tu valor es una consonante")

alumno = input("Favor de ingresar un caracter: ")
maestro(alumno)
"""
#Me falta usar listas para que el código sea mucho más fácil de leer y más liviano.

#Decirle al usuario que ingrese dos números y que nos devuelva el mayor de estos:
"""def mayor_menor(a, b):
    if a > b:
        return print(f"{a} es mayor")
    elif a == b:
        return print("Los números son iguales")
    else:
        return print(f"{b} es mayor")
n1 = int(input("Ingresa tu primer número: ")) 
n2 = int(input("Ingresa tu segundo número: ")) 
mayor_menor(n1, n2)"""
#Esta todo bastante bien logrado, poniendo f"{}" puedo poner el valor dado por el usuario en lugar de solo ponerle "el primer valor fue mayor".

#Determinar si un número es múltiplo de 3 y 5.
"""def select(n):
    if n % 3 == 0 ** n % 5 == 0:
      return print("Tú número si es multiplo de 3 y 5")
    else:
      return print("No es multiplo de 3 y 5")
nn = int(input("Favor de ingresar un número entero: "))
select(nn)"""
#Revisar la operación matematica y el problema, pues lo encuentro algo difuso.

#Determina si un número entero es par o impar:
"""def par(n):
    if n % 2 == 0:
        return print(f"{n} es par")
    else:
        return print(f"{n} es impar")
p = int(input("Favor de ingresar un número entero: "))
par(p)"""
#gg's

#Haz un programa que de tres números dados por el usuario de el mayor.
"""def mayorde3(a, b, c):
    if a > b:
        if a > c:
            return print(f"{a} es mayor")
        else:
            return print(f"{c} es mayor")
    elif a == b:
        return print("Los números son iguales")
    else:
        if b > c:
            return print(f"{b} es mayor")
        else:
            return print(f"{c} es mayor")
n1 = int(input("Ingresa tu primer número: ")) 
n2 = int(input("Ingresa tu segundo número: ")) 
n3 = int(input("Ingresa tu tercer número: ")) 
mayorde3(n1, n2, n3)"""
#Sirvió para entender un poco mejor las expresiones anidadas.

#Pedir un número, si es par lo duplica, si no, lo triplica:
"""def par(n):
    if n % 2 == 0:
        #n = n * 2
        return print(f"El doble de {n} es {n*2}")
    else:
        #n = n * 3
        return print(f"El triple de {n} es {n*3}")
nn = int(input("Favor de ingresar un número entero: "))
par(nn)"""
#Yo lo había hecho de una manera más extensa, pero un usuario simplifico todo, poniendo las multiplicaciones dentro del print, cosa que había olvidado.

#El usuario ingresa tres números y te los devuelve en orden ascendente.
#Buscamos el número mayor:
# def ordena3(a, b, c):
#     if a > b and a > c:
#         mayor = a
#     else:
#         if b > a and b > c:
#             mayor = b
#         else:
#             mayor = c
# #Buscamos el menor 
#     if a < b and a < c:
#         menor = a
#     else:
#         if b < a and b < c:
#             menor = b 
#         else:
#             menor = c
# #Buscamos el intermedio 
#     intermedio = (a + b + c) - (mayor + menor)
#     return print(f"""El orden de tus números es:
#     Mayor: {mayor}
#     Intermedio: {intermedio}
#     Menor: {menor}""")

# n1 = int(input("Ingresa tu primer número: ")) 
# n2 = int(input("Ingresa tu segundo número: ")) 
# n3 = int(input("Ingresa tu tercer número: ")) 
# ordena3(n1, n2, n3)
#Si tuve complicaciones, pero nada grave.

#Que el usuario ingrese un número de 1 al 4 y regrese una estación del año:
    #1-Verano, 2-Otoño, 3-Invierno, 4-Primavera.
"""def estacion(a):
    if a == 1:
        return print("Verano")
    elif a == 2:
        return print("Otoño")
    elif a == 3:
        return print("Invierno")
    elif a == 4:
        return print("Primavera")
    else:
        return print("Valor no valido")
n = int(input("Favor de ingresar un número del 1 al 4: "))
estacion(n)"""
#gg's

#El número que el usuario ingrese del 0 al 9 devuelvelo en letras:
"""def num(a):
    if a == 0:
        return print("Cero")
    elif a == 1:
        return print("Uno")
    elif a == 2:
        return print("Dos")
    elif a == 3:
        return print("Tres")
    elif a == 4:
        return print("Cuatro")
    elif a == 5:
        return print("Cinco")
    elif a == 6:
        return print("Seis")
    elif a == 7:
        return print("Siete")
    elif a == 8:
        return print("Ocho")
    elif a == 9:
        return print("Nueve")
    else:
        return print("Valor no valido")
n = int(input("Favor de ingresar un número del 0 al 9: "))
num(n)"""
#gg's

#Calculadora:
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
#gg's

#Ingresa un número del mes y ten una estación:
# def estacion(a):
#     if a == 1 or a == 2 or a == 3:
#         return print("Verano")
#     elif a == 4 or a == 5 or a == 6:
#         return print("Otoño")
#     elif a == 7 or a == 8 or a == 9:
#         return print("Invierno")
#     elif a == 10 or a == 11 or a == 12:
#         return print("Primavera")
#     else:
#         return print("Valor no valido")
# n = int(input("Ingresa un número del 1 al 12 según el mes para saber la estación del año: "))
# estacion(n)
#GG's