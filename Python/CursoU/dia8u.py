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
