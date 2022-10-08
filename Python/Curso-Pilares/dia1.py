from array import array
from multiprocessing import Array

# Ejercicio 1: Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!
print("Hola Mundo")

# Ejercicio 2: Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable
# y luego muestre por pantalla el contenido de la variable.
HM = str("Hola Mundo")
print(HM)

# Ejercicio 3: Escribir un programa que pregunte al usuario por el número de horas trabajadas
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
tiempo = int(input("¿Cuántas horas trabajaste? "))
costo = int(input("¿Cuánto ganas por hora? "))
print(tiempo * costo)

# Escribir un programa que lea un entero positivo, introducido por el usuario y después
# muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los primeros
# enteros positivos puede ser calculada de la siguiente forma: SUMA = n(n+1)/2
n = int(input("Ingresa un número: "))


# Ejercicio 5
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla
# la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal
# calculado redondeado con dos decimales.
kg = int(input("Ingresa tu peso en kilogramos: "))
cm = int(input("Ingresa tu altura en centimetros: "))
masa_corporal = (kg) / cm ** 2
mc = masa_corporal * 10000 #Lo que estoy haciendo con esto es poder recorrer decimales para dar un número y decimales, en lugar de puros decimales
print(f"Tú indice de masa corporal es: {mc:.2f}")

# Ejercicio 6
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.


# Ejercicio 7
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al
# año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden
# al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la
# cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el
# primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
ahorro = int(input("Cuánto deseas abonar a tu cuenta de ahorro? "))
interes = 1.04
pa = ahorro * interes
sa = pa * interes
ta = sa * interes
print(f"Tu ahorro en el primer año es de: {pa:.2f}")
print(f"Tu ahorro en el segundo año es de: {sa:.2f}")
print(f"Tu ahorro en el tercer año es de: {ta:.2f}")
