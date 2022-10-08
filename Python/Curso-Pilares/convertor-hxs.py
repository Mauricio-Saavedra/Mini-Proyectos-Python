#Este pequeño programa lo que hace es converir un valor que se asume son horas en los segundos que hay dentro de ella.
horas = int(input("Dame las horas a convertir "))
Segundos = horas * 60 * 60
print("Los segundos que hay en ese tiempo son: " ,Segundos)

#Acá va el problema de la raíz cuadrada:
valor = int(input("Dame el número que deseas ver al cuadrado, al cubo y su raíz cuadrada: "))
print(valor ** 2)
print(valor ** 3)
print(valor ** .5)

#Acá vamos a solicitar los valores de Base y Altura de un Triangulo Rectangulo para calcular su hipotenusa: formula=  base al cuadrado + altura al cuadrado = hipotenusa al cuadrado, por ende uno debe de sacarle la raíz cuadrado a ese resultado.
b = int(input("Dame la base de tu triangulo: "))
h = int(input("Dame la altura de tu triangulo: "))
Hipotenusa = (b ** 2) + (h ** 2) #Cuando hacemos esa operación saca su potencia 2
print(Hipotenusa ** .5) 

#Calcula la media de 5 números dados por el usuario:
n1 = int(input("Dame tú 1er número: "))
n2 = int(input("Dame tú 2do número: "))
n3 = int(input("Dame tú 3er número: "))
n4 = int(input("Dame tú 4to número: "))
n5 = int(input("Dame tú 5to número: "))
print((n1 + n2 + n3 + n4 + n5) / 5)