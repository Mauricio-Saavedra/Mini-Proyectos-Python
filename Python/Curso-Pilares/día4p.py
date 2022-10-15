
#Ejercicio 1 de lo visto la semana pasada
#Haz una función que detecte si un string es un palindromo:
"""
def palindromo (f):
    if f == f[::-1]:
        return "Es un palindromo"
    else:
        return "No es un palindromo"

pal = input("Ingresa tu frase o palabra: ").upper().replace(" ", "")
print(palindromo(pal))
"""
#Lo que sucedio aquí es que:
    #pal es igual a un string por el input...
    #...cuando acaba ese input() sigue siendo un string, por ende podemos ponerle otro metodo:
    #   input().upper() -> UPPER() lo estamos ocupando para que transforme los caracteres dentro del strin en Mayusculas.
    #Después debemos emilinar los espacios, pues aunque nosotros sabemos que es un palindromo, la computadora no lo registra así, por ello debemos quitarle los espacios.
    #   input().upper().replace(" ", "") -> Con REPLACE() estamos reemplazando el valor " ", por nada "".

#Ejercicio uno de la clase de hoy.
#Cliclo FOR: es un ciclo iterador (un iterable es cuando se puede itrerar dentro de cualquier colección que se pueda recorrer: string, tupla, diccionarios, rangos).
# RANGE establece un rango, en este caso 10.
# i será la variable que ira tomando el valor de nuestro iterable 10, primero 0, luego 1, luefo 2, etc...
"""
for i in range(10): #Harás que esta "i" recorra el elemento RANGE.
    print(i)
#El resultado de esto sería: 0,1,2,3,4,5,6,7,8,9. Pues toma 10 valores
for i in range(1, 15):
    print(i)

#Un ejemplo del recorrido que da "i" es el siguiente:
for i in "edgar":
    print("hola")
#Como podemos ver nos imprime "hola" 5 veces, una por cada letra de e-d-g-a-r.
    #Entonces la "i" hace un recorrido por el dato que nosotros le presentemos.
for i in ("hola", "edgar"):
    print("hola")
"""
#Acá al ser una tupla recorre dos veces una vez por cada elemento de la tupla.

#Segundos ejercicios del día:
"""
for i in range(0, 51, 3): #(Valor de inicio, Valor de final, valor de salto[En este caso de tres en tres])
    print(i)

#Haz una lista que contenga los números del 1 al 50 con FOR:
lista = []
for i in range(1, 51):
    lista.append(i) #Recuerda que APPEND() añade un valor al final de la lista, y el valor a agregar es el que "i" tenga en ese momento.

print(lista)
"""
#Cilco WHILE: El concepto detras de un ciclo whil ees simple:
    # Mientras una condición en verdadera -> Ejecuta mis comandos.
#El bucle while comprueba la condición cada vez, y si esta condiciión devuelve un True, ejecutará las instrucciones dentro del bucle.
"""
x = 1           #Declaramos un variable "x".
while x <= 10:  #Mientras "x" sea menor a 10 tu...
    print(x)    #...imprimiras el valor de "x", y...
    x += 1      #...Le sumarás 1 a "x"
else:           #Acá el ELSE esta a la par del WHILE, y es posible ocuparla, aunque no sea muy habitual.
    print("Done")
"""
#Vamos a pedir 5 calificaicones entre 0 y 10, después las acumulamos y le sacamos el promedio, si el promedio es menor a siete "reprobo", si es mayor "aprovado":
#Vamos a declarar la variable ACUMULADOR para ir sumando las calificaciones:
"""
acumulador = 0
#Después vamos a usar un FOR para delimitar el rango de las calificaciones con el RANGE:
for i in range(1, 6):
    #Pedimos la calificación al usuario:
    calificación = int(input(f"Ingresa tu calificación {i}: "))
    #MIENTRAS el valor de CALIFICACION sea menor a 0 o mayor a 10...
    while calificación < 0 or calificación > 10:
        #...IMPRIMIRAS:
        print("Calificación no valida.")
        #Y volverás a pedir la califiación, para que sigamos pidiendola hasta que el usuario dé una calificación valida:
        calificación = int(input(f"Ingresa tu calificación {i}: "))
    #Ahora que la califiación es valida esta se sumará al acumulador.
    acumulador += calificación
#Después guardaremos en la variable promedio el resultado de acumulador entre 5:
promedio = acumulador/5
#Si el contenido de promedio es menor a 7, le dirás que no aprueba:
if promedio < 7:
    print(f"Tu promedio es de:{promedio}, Vas pa'tras.")
#SINO entonces le dices que esta aprovado:
else:    
    print(f"Tú promedio es de:{promedio}, ¡Aprobaste!")
"""