# PRACTICA 6: REALIZA LOS SIGUIENTES PROGRAMAS
# 1.-Realizar un menú, donde podemos escoger las distintas opciones de operaciones
# (multiplicación de dos números, raiz cuadrada de un número, cubo de un número y división
# de dos números) hasta que seleccionamos la opción de “Salir”.
"""
cont = 0
while cont != 8:
    print('Bienvenido a mi segunda calculadora, por favor selecciona una de las siguientes operaciones:\n1-Suma.\n2-Resta.\n3-Multiplicación.\n4-División.\n5-potencia.\n6-Modulo.\n7-Raíz cuadrada.\n8 o más para Salir.')
    cont = int(input('Ingresa el número de la operación a realizar: '))
    if cont >= 8:
        print('Gracias por usar mi calculadora.')
        break
    num1 = int(input('Favor de ingresar tú 1er valor: '))
    if cont == 7:
        print(f'La Raíz cuadrada de {num1} es: {num1 ** .5}')
        continue        
    num2 = int(input('Favor de ingresar tú 2do valor: '))
    if cont == 1:
        print(f'El resultado de sumarle {num1} a {num2} es: {num1 + num2}')
    if cont == 2:
        print(f'El resultado de restarle {num1} a {num2} es: {num2 - num1}')
    if cont == 3:
        print(f'El resultado de multiplicar {num1} por {num2} es: {num1 * num2}')
    if cont == 4:
        print(f'El resultado de dividir {num1} entre {num2} es: {num1 / num2}')
    if cont == 5:
        print(f'La potencia de {num1} elevado a {num2} es: {num1 ** num2}')
    if cont == 6:
        print(f'El modulo {num2} de {num1} es: {num1 % num2}')
"""
# 2.-Pedir al usuario u número y determinar si el número ingresado es primo o no.
"""
primos = [1, 2, 3, 5, 7] #Declaro una lista con los primeros números primos.
for i in range(8, 100):  #En un ciclo voy a llenar esta lista con números primos:
    if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        primos.append(i) #Si él número cumple las condiciones de arriba, o sea que sus modulos de 2,3,5,7
#Para aumentar de manera efectiva la capacidad de números primos, deberia de hacer otro ciclo FOR con la primera ista de número del 1 al 100 y volver a meter en la lista todos aquellos que cumplan las condiciones dentro de un rango  más amplio.
# print(primos)
# print(len(primos))
#Ahora pido el número al usuario, y si este esta dentro de la lista, entonces es un número primo.
num = int(input('Ingresa tú número para saber si es primo o no: '))
if num in primos:
    print('¡Es primo!')
else:
    print('No lo es.')
"""
# 3.-Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
# 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa
# para determinar cuánto debe pagar mensualmente y el total de lo que pagó
# hasta los 20 meses.
"""
costo = 10
meses = 1
contenedor = []
while meses != 20:
    contenedor.append(costo)
    print(f'Mes: {meses}. Pago: {costo}')
    costo += costo
    meses += 1
print(f'Mes: {meses}. Pago: {costo}')
total = sum(contenedor) + costo
print(f'El total que has pagado es: {total}')
"""
# 4.-Crea un programa que pida un número y calcule su factorial (El factorial de un
# número es el producto de todos los enteros entre 1 y el propio número y se
# representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
# 1x2x3x4x5=120).
"""
num1 = int(input('Ingresa un número para saber su factorial: '))
num1 += 1
num2 = 1
for i in range(1, num1):
    num2 *= i 
print(f'El factorial "n!" de tú número es: {num2}')
"""