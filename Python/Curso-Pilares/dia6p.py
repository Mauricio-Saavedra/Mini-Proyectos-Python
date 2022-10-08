#Listas comprimidas del día 6:
#Metodo: Función que pertenecé a un objeto, .append() pertenece a las listas.
#1.-Crea una lista que contenga los multiplos de 5 al cuadrado:
"""
lista = []
cont = 0
cuadrado = 0
for i in range(101):
  if i % 5 == 0:
    cont = i
    cuadrado = cont**2
    lista.append(cuadrado)
print(f"{lista}\n")
"""
#Otra manerá más rápida de hacerlo es esta:
"""
lista2 = []
for ii in range(5, 101, 5):
  lista2.append(ii * ii)
print(f"Lista simplificada:{lista2}\n")
#Pues acá estamos dando en el rango(número inicial, final, salto)
#Y es con este salto que ya no debemos hacer el modulo.
#Ya dentro del .append(tenemos el número del rang multiplicado por si mismo)
"""
#Las compresiones de listas nos proporcionan una forma corta y conscisa de crear listas. Se usan con [] y en su interior contienen una EXPRESION seguida de un bucle FOR y cero o más sentencias FOR o IF, lo que significa que puedes usar cualquier tipo de objetos en lalista. El resultado es una nueva lista creada tras evaluar als expresiones uqe haya dentro.
#Sintaxis:
#[elemento FOR elemento IN iterable IF condición]
"""
comprimida = [i * i for i in range(0, 101, 5)]
print(f'Esta es la comprimida:{comprimida}\n')

#La anterior, pero ahora con una condicional:
comprimida2 = [i * i for i in range(0, 101, 5) if i % 5 == 0]
print(f'Esta es la comprimida con una condicional:{comprimida2}')
"""
#2-Llena una lista comprimida con los números que sean multiplos de 4 que a la vez sean multiplod de 6,
#hasta qu elos números sean menores a 5 digitos:
"""
print("Este es el ejercicio:")
comprimida3 = [
  i for i in range(99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0
]
print(f'Esta es la comprimida con una condicional:{comprimida3}')
#Las listas comprimidas pueden usarse cuando tenga:
  #Lista vacia
  #ciclo, pero mas sencillo con for
  #append()
"""
#Diccionarios comprimidos, sintaxis:
#{Key:Value FOR value IN iterable IF condición}
#Solo se puedes hacer diccionarios así si el valor depende (o se genera a partir) de la llave, o viceversa.

#3.-Llena un diccionario dónde las llaves serán los números pares (0, 100) y los valores asociados a esas llaves serán las llaves elevadas al cuadrado:
diccionario = {i: i * i for i in range(101) if i % 2 == 0}
print(diccionario)
#En la definicióin "i:i*i" estamos diciendo que la llave(i) y el valor(i*i) dependerán de la variable que recorrerá el rango, y se llenará "SI i % 2 == 0" se cumple la condición.