#Funciones:
# Ejercicio1: Crea una función para sumar los valores recibidos de tipo numérico,
# utilizando argumentos variables '*args' como parámetro de la función, y regresa como resultado la suma de todos
# los valores pasados como argumentos:
"""
def sumarValores(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sumarValores(9,9,9))
"""
# Ejercicio2: Crea una función para multiplicar los valores recibidos de un tipo numérico,
# utilizando argumentos variables '*args' como parametros de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumentos:
"""
def multiplacionVal(*args):
    total = 1
    for i in args:
        total *= i
    return total

print(multiplacionVal(9,9,9))
"""
#Funciones Recursivas:
#Una función recursiva es una función que se manda a llamar a si misma para completar una cierta tarea.
	#Un ejemplo que se suele ocupar para esto es sacar el factorial de un número.
	#El factorial de 5 se representa 5! = 5 * 4 * 3 * 2 * 1
"""
def factorial(numero):
	if numero == 1:
		return 1
	else:
		return numero * factorial(numero-1)
resultado = factorial(5)
print(resultado)
"""
# Ejercicio3: Imprimir numeros del 5 al 1 de manera descendente usando funciones recursivas.
# Puede ser cualquier valor positivo, ejemplo, 5,4,3,2,1 o 3,2,1.
"""
def descendente(num):
    if num >= 1:
        print(num)
        descendente(num - 1)
descendente(10)
"""
# Ejercicio4: calculadora de impuestos: Crea una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pagoTotal = pagoSinImpuesto + (pagoSinImpuesto * (impuesto/100))
    #Así lo hice yo:
"""
pagoSinImpuesto = int(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
def calculadoraImp(pago, imp):
    total = 0
    subTotal = pago * imp
    total = subTotal + pago
    return total
print(calculadoraImp(pagoSinImpuesto, impuesto))
"""
    #Así lo hizo el profe:
"""
def calculadoraTotalPago(pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return pagoTotal
pagoSinImpuesto = int(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
pagoConImpuesto = calculadoraTotalPago(pagoSinImpuesto, impuesto)
print(f'El pago con impuesto es: {pagoConImpuesto}')
    #Lo hizo con una línea de código menos xd, pero lo importante es que su función se ve más limpía.
"""
#Ejercicio5: Realiza dos funciones, una para convertir de °Celcius a °Fahrenheit y viceversa:
    #Siento que me quedó bien.
"""
gradosFah = float(input('Ingresa los °fahrenheit que quieres convertir: '))
gradosCel = float(input('Ingresa los °celcius que quieres convertir: '))

def celciusToFah(fah):
    cel = (fah * 1.8) + 32
    return cel

def fahrenToCel(cel):
    fah = (cel -32) / 1.8
    return fah

print(f'Los °{gradosFah} Fahrenheit en °Celcius son: {fahrenToCel(gradosFah)}')
print(f'Los °{gradosCel} Celcius en °Fahrenheit son: {celciusToFah(gradosCel)}')
"""
# Funciones lambda:
# También son llamadas "Funciones anonimas.
# Estas funciones son utilizadas para expresiones pequeñas que se pueden ocupar en cualquier lugar, y son de una sola expresión.
# Sintaxis:
"""
suma = lambda a,b:a+b
print(suma(10,20))
# Más ejemplos de lambda:
duplicar = lambda n: n*2
par = lambda n: n % 2 == 0
impar = lambda n: n % 2 != 0
revertir = lambda cadena: cadena[::-1]
"""
# Como ves funcionan para consas sencillas, si son de un solo uso, haz una lambda, si es recurrente, si crea la función.
"""
x = lambda cadena: cadena[::-3]
print(x('mundo'))
# Más ejemplos de lambda:
duplicar = lambda n: n*2
par = lambda n: n % 2 == 0
impar = lambda n: n % 2 != 0
revertir = lambda cadena: cadena[::-1]
"""
#Practica1: Palindromo, crea un programa al cual se le sea imgresado un string y te diga si es un palindromo o no.
"""
palindromo = input('Ingresa una palabra para saber si es un palindromo:\n').lower().replace(' ', '')
if palindromo == palindromo[::-1]:
    print('Es Palindromo!')
else:
    print('No es Palindromo :c')
""" #GG's
#Practica2: Primalidad, crea un sistema que detecte si un número ingresado po rteclado es primo o no.
"""
primos = [1,2,3,5,7]
num = int(input('Ingresa un número para saber si es primo: '))
for i in range(8,100):
    if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        primos.append(i)
if num in primos:
    print('¡Número norteño!')
else:
    print('No es norteño')
"""
#Practica3: Generador de contraseñas, Crea un sistema que genere contraseñas aleatorias.
# Se requiere: lista, lista mayuscula, lista minuscula, lista números y lista de simbolos, y luego armar una contraseña aleatoria sacando caracteres de estas listas:
"""
import random
import secrets

mayu = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
mini = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','p','q','r','s','t','u','v','w','x','y','z']
nums = [1,2,3,4,5,6,7,8,9,0]
char = ['!','#','$','%','&','+','*','-','_']
cont = []
digt = int(input('Cuantos caracteres necesitas para tu contraseña: '))
for i in range(digt):
    x = random.randrange(1,4)
    if x == 1:
        x = mayu
    elif x == 2:
        x = mini
    elif x == 3:
        x = nums
    elif x == 4:
        x = char
    y = secrets.choice(x)
    cont.append(y)
contraseña = str(cont).replace(',','').replace(' ','').replace("'","")
print(f'Tú nueva contaseña es: {contraseña}')
"""
# El módulo de secrets se usa esencialmente para el mismo propósito que el de random. Sin embargo, secrets proporciona un método criptográficamente seguro para implementar el PRNG.
# En aplicaciones de la vida real como el almacenamiento de contraseñas, autenticación, cifrado y descifrado, y fichas. secrets es mucho más seguro que el uso de random, ya que sólo sirve para simulaciones u operaciones que no manejen datos sensibles.
"""Aire visual entre ejercicios"""
