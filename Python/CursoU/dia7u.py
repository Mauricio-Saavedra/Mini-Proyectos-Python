
#Ejercicio1: Un restaurante ofrece un descuento del 10% para consumo de hasta $100, y un descuento del 20%
    # para consumos mayores, para ambos casos se ofrece un impuesto del 19%. Determina el monto del impuesto,
    # el descuento y el monto a pagar.
"""
pago = int(input('Ingresa el monto a pagar: '))
if pago > 0 and pago <= 100:
    iva = pago * .19
    des = pago * .10
    total = (pago - iva) - des 
    print(f'El pago de {pago}, tiene:\nUn descuento de: {des}\nUn impuesto de: {iva}\nLo que deja {total} de ganancia.')
if pago > 100:
    iva = pago * .19
    des = pago * .20
    total = (pago - iva) - des 
    print(f'El pago de {pago}, tiene:\nUn descuento de: {des}\nUn impuesto de: {iva}\nLo que deja {total} de ganancia.')
"""
#Ejercicio2: debido a lso excelentes resultados el restaurante decide ampliar sus ofertas de acuerdo a la siguiente escala:
    # hasta 100 -> 10%
    # Mayor 100 -> 20%
    # Mayor 200 -> 30%
"""
pago = int(input('Ingresa el monto a pagar: '))
if pago > 0 and pago <= 100:
    iva = pago * .19
    des = pago * .10
    total = (pago - iva) - des 
    print(f'El pago de {pago}, tiene:\nUn descuento de: {des}\nUn impuesto de: {iva}\nLo que deja {total} de ganancia.')
if pago > 100 and pago < 200:
    iva = pago * .19
    des = pago * .20
    total = (pago - iva) - des 
    print(f'El pago de {pago}, tiene:\nUn descuento de: {des}\nUn impuesto de: {iva}\nLo que deja {total} de ganancia.')
if pago > 200:
    iva = pago * .19
    des = pago * .30
    total = (pago - iva) - des 
    print(f'El pago de {pago}, tiene:\nUn descuento de: {des}\nUn impuesto de: {iva}\nLo que deja {total} de ganancia.')
"""
#Ejercicio3: Crea dos lista sy una tupla que tendra números del 1 al 9.
# La primera lista contendrá números pares y la segunda impares, ambas empiezan vacías.
# Después de multiplicar cada número de la tupla por un número al azar entre 1-100,
# Si el resultado es par se va a su lista, igual si es impar.
# Muestra por consola:
    # La multiplicación que se produce con el formato a x b = c
    # y la lista de pares e impares.

import random

tupla = (1,2,3,4,5,6,7,8,9)
par = []
imp = []
tot = 0
for i in tupla:
    ram = random.randrange(1,100)
    tot = i * ram
    print(f'{i} x {ram} = {tot}')
    if tot % 2 == 0:
        par.append(tot)
    else:
        imp.append(tot)
print(f'->Los restultados pares son: {par}\nLos resultados impares son: {imp}')